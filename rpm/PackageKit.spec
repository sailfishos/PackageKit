# Conditional building of X11 related things
%bcond_with X11

%define glib2_version           2.20.0
%define dbus_version            1.1.3
%define dbus_glib_version       0.74
%define policykit_version       0.92

# Vendor-specific values displayed in PackageKit user interfaces
%define vendor_name             Mer
%define vendor_bugs             http://bugs.merproject.org/
%define vendor_icon             mer-logo-small

Summary:   Package management service
Name:      PackageKit
Version:   0.8.9
Release:   1
License:   GPLv2+
Group:     System/Libraries
URL:       http://www.packagekit.org
Source0:   http://www.packagekit.org/releases/%{name}-%{version}.tar.gz
Source100: rpm-db-clean.service
Source101: pk-rpm-db-clean
Source102: pk-zypp-cache.conf

Requires: PackageKit-zypp = %{version}-%{release}
Requires: shared-mime-info
Requires: connman

BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: dbus-devel  >= %{dbus_version}
BuildRequires: dbus-glib-devel >= %{dbus_glib_version}
BuildRequires: pam-devel
%if %{with X11}
BuildRequires: libX11-devel
BuildRequires: pango-devel
%endif
BuildRequires: sqlite-devel
BuildRequires: connman-devel
BuildRequires: polkit-devel >= %{policykit_version}
BuildRequires: libtool
BuildRequires: python-devel
BuildRequires: perl(XML::Parser)
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: libgudev1-devel
BuildRequires: libarchive-devel
BuildRequires: gstreamer-devel
BuildRequires: gst-plugins-base-devel
BuildRequires: fontconfig-devel
BuildRequires: libzypp-devel >= 5.20.0
BuildRequires: bzip2-devel
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(mce)
# FIXME, blows up, as this piece of shit downloads stuff from sourceforge
#BuildRequires: libxslt

%description
PackageKit is a D-Bus abstraction layer that allows the session user
to manage packages in a secure way using a cross-distro,
cross-architecture API.

%package zypp
Summary: PackageKit zypp backend
Group: System/Libraries
Requires: libzypp >= 5.20.0
Requires: %{name} = %{version}-%{release}

%description zypp
A backend for PackageKit to enable zypp functionality.

%package docs
Summary: Documentation for PackageKit
Group: Documentation
Requires: %{name} = %{version}-%{release}

%description docs
%{summary}.

%package glib
Summary: GLib libraries for accessing PackageKit
License: LGPLv2+
Group: System/Libraries
Requires: dbus >= %{dbus_version}
Requires: %{name} = %{version}-%{release}
Obsoletes: PackageKit-libs < %{version}-%{release}
Provides: PackageKit-libs = %{version}-%{release}

%description glib
GLib libraries for accessing PackageKit.

%package python
Summary: Python libraries for accessing PackageKit
License: LGPLv2+
Group: System/Libraries
Requires: %{name} = %{version}-%{release}

%description python
Python libraries for accessing PackageKit.

%package cron
Summary: Cron job and related utilities for PackageKit
Group: System/Base
Requires: cronie
Requires: %{name} = %{version}-%{release}

%description cron
Crontab and utilities for running PackageKit as a cron job.

%package debug-install
Summary: Facility to install debugging packages using PackageKit
Group: System/Base
Requires: %{name} = %{version}-%{release}
Obsoletes: PackageKit-debuginfo-install <= 0.5.2-0.1.20090902git.fc12

%description debug-install
Provides facility to install debugging packages using PackageKit.

%package glib-devel
Summary: GLib Libraries and headers for PackageKit
License: LGPLv2+
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: dbus-devel >= %{dbus_version}
Requires: pkgconfig
Requires: sqlite-devel
Requires: PackageKit-glib = %{version}-%{release}
Obsoletes: PackageKit-devel < %{version}-%{release}
Provides: PackageKit-devel = %{version}-%{release}

%description glib-devel
GLib headers and libraries for PackageKit.


%package plugin-devel
Summary: Headers to compile out of tree PackageKit plugins
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description plugin-devel
Headers to compile out of tree PackageKit plugins.

%package gstreamer-plugin
Summary: Install GStreamer codecs using PackageKit
Group: System/Libraries
Requires: gstreamer
Requires: PackageKit-glib = %{version}-%{release}

%description gstreamer-plugin
The PackageKit GStreamer plugin allows any Gstreamer application to install
codecs from configured repositories using PackageKit.

%package command-not-found
Summary: Ask the user to install command line programs automatically
Group: System/Libraries
Requires: bash
Requires: PackageKit-glib = %{version}-%{release}

%description command-not-found
A simple helper that offers to install new packages on the command line
using PackageKit.

%package device-rebind
Summary: Device rebind functionality for PackageKit
Group: System/Libraries
Requires: PackageKit-glib = %{version}-%{release}

%description device-rebind
The device rebind functionality offer the ability to re-initialize devices
after firmware has been installed by PackageKit. This removes the need for the
user to restart the computer or remove and re-insert the device.


%prep
%setup -q -n %{name}-%{version}/PackageKit

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

export LIBS=-ldbus-glib-1
%configure \
        --disable-static \
        --disable-dummy \
        --enable-zypp \
        --with-default-backend=zypp \
        --enable-mce \
        --disable-local \
        --disable-strict \
        --disable-networkmanager \
        --disable-gtk-doc-html \
        --disable-man-pages \
        --disable-tests \
%if %{with X11}
        --enable-browser-plugin \
%endif
        --disable-bash_completion

make %{?_smp_mflags}

%install

export PATH=$PATH:`pwd`/hack
%make_install

touch $RPM_BUILD_ROOT%{_localstatedir}/cache/PackageKit/groups.sqlite

# create a link that GStreamer will recognise
pushd ${RPM_BUILD_ROOT}%{_libexecdir} > /dev/null
ln -s pk-gstreamer-install gst-install-plugins-helper
popd > /dev/null

# create a link that from the comps icons to PK, as PackageKit frontends
# cannot add /usr/share/pixmaps/comps to the icon search path as some distros
# do not use comps. Patching this in the frontend is not a good idea, as there
# are multiple frontends in multiple programming languages.
pushd ${RPM_BUILD_ROOT}%{_datadir}/PackageKit > /dev/null
ln -s ../pixmaps/comps icons
popd > /dev/null

# Remove docs
rm -rf %{buildroot}/usr/share/gtk-doc/ %{buildroot}/usr/share/PackageKit/website/

# Add vendor-specific values to system configuration
sed -i \
    -e 's#^\(DefaultUrl=\).*$#\1%{vendor_bugs}#g' \
    -e 's#^\(VendorName=\).*$#\1%{vendor_name}#g' \
    -e 's#^\(VendorIcon=\).*$#\1%{vendor_icon}#g' \
    ${RPM_BUILD_ROOT}%{_sysconfdir}/PackageKit/Vendor.conf

# Enable runtime support for connman
sed -i \
    -e 's#^\(UseNetworkConnman=\).*$#\1true#g' \
    ${RPM_BUILD_ROOT}%{_sysconfdir}/PackageKit/PackageKit.conf

# install cleanup service files
install -D -m 644 %{S:100} %{buildroot}%{_unitdir}/rpm-db-clean.service
install -D -m 755 %{S:101} %{buildroot}%{_libexecdir}/pk-rpm-db-clean

# install dist-upgrade libzypp config file
install -D -m 644 %{S:102} %{buildroot}%{_sysconfdir}/zypp/pk-zypp-cache.conf

# add hardcoded arch entry to pk-zypp-cache.conf (JB#28277)
# needed only for armv7hl-on-armv7l kernel
%ifarch armv7hl
echo "arch = armv7hl" >>%{buildroot}%{_sysconfdir}/zypp/pk-zypp-cache.conf
%endif

%find_lang %name

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
%doc README AUTHORS  COPYING
%dir %{_datadir}/PackageKit
%dir %{_datadir}/PackageKit/helpers
%dir %{_sysconfdir}/PackageKit
%dir %{_sysconfdir}/PackageKit/events
%dir %{_sysconfdir}/PackageKit/events/post-transaction.d
%dir %{_sysconfdir}/PackageKit/events/pre-transaction.d
%{_sysconfdir}/PackageKit/events/*.d/README
%dir %{_localstatedir}/lib/PackageKit
%dir %{_localstatedir}/cache/PackageKit
%ghost %verify(not md5 size mtime) %{_localstatedir}/cache/PackageKit/groups.sqlite
%dir %{_localstatedir}/cache/PackageKit/downloads
%dir %{_libdir}/packagekit-backend
%config(noreplace) %{_sysconfdir}/PackageKit/*.conf
%config %{_sysconfdir}/dbus-1/system.d/*
%dir %{_datadir}/PackageKit/helpers/test_spawn
%dir %{_datadir}/PackageKit/icons
%{_datadir}/PackageKit/helpers/test_spawn/*
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/mime/packages/packagekit-*.xml
%{_datadir}/PackageKit/pk-upgrade-distro.sh
%{_libexecdir}/packagekitd
%{_bindir}/pkmon
%{_bindir}/pkcon
%{_bindir}/pkgenpack
%{_bindir}/packagekit-bugreport.sh
%exclude %{_libdir}/libpackagekit*.so.*
%{_libdir}/packagekit-backend/libpk_backend_test_*.so
%ghost %verify(not md5 size mtime) %{_localstatedir}/lib/PackageKit/transactions.db
%{_datadir}/dbus-1/system-services/*.service
%{_libdir}/packagekit-plugins/*.so
%{_datadir}/dbus-1/interfaces/*.xml
/lib/systemd/system/packagekit-offline-update.service
%{_libexecdir}/pk-clear-offline-update
%{_libexecdir}/pk-offline-update
%{_libexecdir}/pk-trigger-offline-update

%files docs
%defattr(-,root,root,-)
%doc README AUTHORS  COPYING
#%{_mandir}/man1/*

%files zypp
%defattr(-,root,root,-)
%doc README AUTHORS  COPYING
%{_libdir}/packagekit-backend/libpk_backend_zypp.so
%{_libexecdir}/pk-rpm-db-clean
%{_unitdir}/rpm-db-clean.service
%config %{_sysconfdir}/zypp/pk-zypp-cache.conf

%files glib
%defattr(-,root,root,-)
%doc README AUTHORS  COPYING
%{_libdir}/*packagekit-glib*.so.*

%files python
%defattr(-,root,root,-)
%doc README AUTHORS  COPYING
%dir %{python_sitelib}/packagekit
%{python_sitelib}/packagekit/*py*

%files cron
%defattr(-,root,root,-)
%doc README AUTHORS  COPYING
%config %{_sysconfdir}/cron.daily/packagekit-background.cron
%config(noreplace) %{_sysconfdir}/sysconfig/packagekit-background

%files debug-install
%defattr(-,root,root,-)
%doc README AUTHORS  COPYING
%{_bindir}/pk-debuginfo-install

%files gstreamer-plugin
%defattr(-,root,root,-)
%doc README AUTHORS  COPYING
%{_libexecdir}/pk-gstreamer-install
%{_libexecdir}/gst-install-plugins-helper

%files command-not-found
%defattr(-,root,root,-)
%doc README AUTHORS  COPYING
%{_sysconfdir}/profile.d/*
%{_libexecdir}/pk-command-not-found
%config(noreplace) %{_sysconfdir}/PackageKit/CommandNotFound.conf

%files device-rebind
%defattr(-,root,root,-)
%doc README AUTHORS  COPYING
%{_sbindir}/pk-device-rebind

%files glib-devel
%defattr(-,root,root,-)
%doc README AUTHORS  COPYING
%{_libdir}/libpackagekit-glib*.so
%{_libdir}/pkgconfig/packagekit-glib2.pc
%dir %{_includedir}/PackageKit
%dir %{_includedir}/PackageKit/packagekit-glib2
%{_includedir}/PackageKit/packagekit-glib*/*.h

%files plugin-devel
%defattr(-,root,root,-)
%doc README AUTHORS  COPYING
%dir %{_includedir}/PackageKit
%{_includedir}/PackageKit/plugin/*.h
%{_libdir}/pkgconfig/packagekit-plugin.pc
