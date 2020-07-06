# Vendor-specific values displayed in PackageKit user interfaces
%define vendor_bugs             http://bugs.merproject.org/

Summary:   Package management service
Name:      PackageKit
Version:   1.1.13
Release:   1
License:   GPLv2+ and LGPLv2.1+
URL:       https://www.freedesktop.org/software/PackageKit/
Source0:   http://www.freedesktop.org/software/PackageKit/releases/%{name}-%{version}.tar.xz
Source100: rpm-db-clean.service
Source101: pk-rpm-db-clean
Source102: packagekit-zypp-override.conf

Requires: PackageKit-zypp = %{version}-%{release}
Requires: shared-mime-info
Requires: sailfish-setup

BuildRequires: glib2-devel >= 2.46
BuildRequires: pam-devel
BuildRequires: sqlite-devel
BuildRequires: polkit-devel >= 0.98
BuildRequires: libtool
BuildRequires: perl(XML::Parser)
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: libarchive-devel
BuildRequires: fontconfig-devel
BuildRequires: libzypp-devel >= 5.20.0
BuildRequires: bzip2-devel
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(mce)
BuildRequires: gobject-introspection-devel
BuildRequires: vala-devel
BuildRequires: autoconf-archive

Obsoletes: PackageKit-python
Obsoletes: PackageKit-debug-install
Obsoletes: PackageKit-plugin-devel

%description
PackageKit is a D-Bus abstraction layer that allows the session user
to manage packages in a secure way using a cross-distro,
cross-architecture API.

%package zypp
Summary: PackageKit zypp backend
Requires: libzypp >= 5.20.0
Requires: %{name} = %{version}-%{release}

%description zypp
A backend for PackageKit to enable zypp functionality.

%package doc
Summary: Documentation for PackageKit
Requires: %{name} = %{version}-%{release}
Obsoletes: %{name}-docs

%description doc
%{summary}.

%package glib
Summary: GLib libraries for accessing PackageKit
License: LGPLv2+
Requires: %{name} = %{version}-%{release}

%description glib
GLib libraries for accessing PackageKit.

%package glib-devel
Summary: GLib Libraries and headers for PackageKit
License: LGPLv2+
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: sqlite-devel
Requires: %{name}-glib = %{version}-%{release}

%description glib-devel
GLib headers and libraries for PackageKit.

%package command-not-found
Summary: Ask the user to install command line programs automatically
Requires: bash
Requires: %{name}-glib = %{version}-%{release}

%description command-not-found
A simple helper that offers to install new packages on the command line
using PackageKit.

%prep
%setup -q -n %{name}-%{version}

%build
# Fix autotools-related issues with Git checkout timestamps, adapted from:
# http://www.gnu.org/software/automake/manual/html_node/CVS.html#All-Files-in-CVS
# (see also: http://stackoverflow.com/questions/934051)
for aclocal_file in $(find . -type f -a -name aclocal.m4); do
    (
        cd $(dirname $aclocal_file)
        sleep 1
        touch aclocal.m4
        sleep 1
        touch configure config.h.in
        sleep 1
        find . -name Makefile.in -exec touch '{}' +
    )
done

./autogen.sh \
        --program-prefix= --prefix=%{_prefix} \
        --exec-prefix=%{_exec_prefix} \
        --bindir=%{_bindir} \
        --sbindir=%{_sbindir} \
        --sysconfdir=%{_sysconfdir} \
        --datadir=%{_datadir} \
        --includedir=%{_includedir} \
        --libdir=%{_libdir} \
        --libexecdir=%{_libexecdir} \
        --localstatedir=%{_localstatedir} \
        --sharedstatedir=%{_sharedstatedir} \
        --with-systemdsystemunitdir=%{_unitdir} \
        --disable-static \
        --disable-dummy \
        --disable-cron \
        --enable-zypp \
        --enable-mce \
        --disable-local \
        --disable-gstreamer-plugin \
        --enable-introspection=no \
        --enable-systemd \
        --disable-man-pages \
        --disable-bash_completion

make %{?_smp_mflags}

%install

export PATH=$PATH:`pwd`/hack
%make_install

# delete unneeded things
rm -r ${RPM_BUILD_ROOT}/%{_datadir}/PackageKit/helpers/test_spawn
rm ${RPM_BUILD_ROOT}/%{_libdir}/packagekit-backend/libpk_backend_test_*.so

# Add vendor-specific values to system configuration
sed -i \
    -e 's#^\(DefaultUrl=\).*$#\1%{vendor_bugs}#g' \
    ${RPM_BUILD_ROOT}%{_sysconfdir}/PackageKit/Vendor.conf

# Enable autoquit
sed -i \
    -e 's/#ShutdownTimeout/ShutdownTimeout/g' \
    ${RPM_BUILD_ROOT}%{_sysconfdir}/PackageKit/PackageKit.conf

# install cleanup service files
install -D -m 644 %{S:100} %{buildroot}%{_unitdir}/rpm-db-clean.service
install -D -m 755 %{S:101} %{buildroot}%{_libexecdir}/pk-rpm-db-clean

# install dist-upgrade libzypp config file
install -D -m 644 %{S:102} %{buildroot}%{_sysconfdir}/zypp/packagekit-zypp-override.conf

# add hardcoded arch entry to packagekit-zypp-override.conf (JB#28277)
# NOTE: zypp.conf might also arch override so this assumes that both files agree on the same value.
echo "arch = %{_target_cpu}" >> %{buildroot}%{_sysconfdir}/zypp/packagekit-zypp-override.conf

%find_lang %name

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
        AUTHORS README NEWS

%post
update-mime-database %{_datadir}/mime &> /dev/null || :

%postun
update-mime-database %{_datadir}/mime &> /dev/null || :

%post glib -p /sbin/ldconfig

%postun glib -p /sbin/ldconfig

%post zypp
/bin/systemctl preset rpm-db-clean.service >/dev/null 2>&1 || :

%preun zypp
%systemd_preun rpm-db-clean.service

%files -f %{name}.lang
%defattr(-,root,root,-)
%license COPYING
%dir %{_datadir}/PackageKit
%dir %{_datadir}/PackageKit/helpers
%dir %{_sysconfdir}/PackageKit
%dir %{_localstatedir}/lib/PackageKit
%dir %{_localstatedir}/cache/PackageKit
%dir %{_localstatedir}/cache/PackageKit/downloads
%dir %{_libdir}/packagekit-backend
%config %{_sysconfdir}/PackageKit/*.conf
%config %{_sysconfdir}/dbus-1/system.d/*
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/polkit-1/rules.d/org.freedesktop.packagekit.rules
# applies only to some desktop distributions
%exclude %{_datadir}/PackageKit/pk-upgrade-distro.sh
%{_libexecdir}/packagekitd
%{_bindir}/pkmon
%{_bindir}/pkcon
%exclude %{_libdir}/libpackagekit*.so.*
%ghost %verify(not md5 size mtime) %{_localstatedir}/lib/PackageKit/transactions.db
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/dbus-1/interfaces/*.xml
%{_unitdir}/packagekit-offline-update.service
%{_unitdir}/packagekit.service
%{_unitdir}/system-update.target.wants/packagekit-offline-update.service
%{_libexecdir}/pk-offline-update
%{_libexecdir}/packagekit-direct

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}

%files zypp
%defattr(-,root,root,-)
%{_libdir}/packagekit-backend/libpk_backend_zypp.so
%{_libexecdir}/pk-rpm-db-clean
%{_unitdir}/rpm-db-clean.service
%config %{_sysconfdir}/zypp/packagekit-zypp-override.conf

%files glib
%defattr(-,root,root,-)
%{_libdir}/*packagekit-glib*.so.*

%files command-not-found
%defattr(-,root,root,-)
%{_sysconfdir}/profile.d/*
%{_libexecdir}/pk-command-not-found
%config %{_sysconfdir}/PackageKit/CommandNotFound.conf

%files glib-devel
%defattr(-,root,root,-)
%{_libdir}/libpackagekit-glib*.so
%{_libdir}/pkgconfig/packagekit-glib2.pc
%dir %{_includedir}/PackageKit
%dir %{_includedir}/PackageKit/packagekit-glib2
%{_includedir}/PackageKit/packagekit-glib*/*.h
