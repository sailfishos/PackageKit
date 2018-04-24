# Vendor-specific values displayed in PackageKit user interfaces
%define vendor_bugs             http://bugs.merproject.org/

Summary:   Package management service
Name:      PackageKit
Version:   1.1.9
Release:   1
License:   GPLv2+ and LGPLv2.1+
Group:     System/Libraries
URL:       https://www.freedesktop.org/software/PackageKit/
Source0:   http://www.freedesktop.org/software/PackageKit/releases/%{name}-%{version}.tar.xz
Source100: rpm-db-clean.service
Source101: pk-rpm-db-clean
Source102: packagekit-zypp-override.conf

Patch1:  0001-Suppress-gtk-doc-building.patch
Patch2:  0002-Comments-out-c-11-14-checks.patch
Patch3:  0003-Comment-out-upstream-usage-of-newer-zypp.patch
Patch4:  0004-Add-support-for-CPU-keepalive-during-transaction.patch
Patch5:  0005-Partly-revert-trivial-Remove-some-unused-functions-o.patch
Patch6:  0006-Builtin-policy-and-whitelist.-Contributes-to-JB-1477.patch
Patch7:  0007-Add-l10n-handler-for-missing-roles.patch
Patch8:  0008-Improve-progress-output-on-non-80x25-terminals.patch
Patch9:  0009-Add-pattern-support.patch
Patch10: 0010-zypp-backend-Implement-upgrade-system-like-zypper-du.patch
Patch11: 0011-Force-repo-refresh-in-pk_backend_refresh_cache.patch
Patch12: 0012-zypp-Backend-Keep-track-of-overall-upgrade-install-p.patch
Patch13: 0013-zypp-Backend-Look-for-patterns-matching-distroId-and.patch
Patch14: 0014-zypp-Backend-Download-progress-reporting.patch
Patch15: 0015-Add-libzypp-authentication-report-handler.patch
Patch16: 0016-zypp-Check-free-space-before-executing-transaction.patch
Patch17: 0017-zypp-Log-messages-into-systemd-journal.patch
Patch18: 0018-zypp-Report-progress-for-download-and-install-separa.patch
Patch19: 0019-zypp-Detect-RPM-database-corruption-for-initializeTa.patch
Patch20: 0020-zypp-Really-really-refresh-when-force-is-set.patch
Patch21: 0021-zypp-Remove-old-leftover-PK_TMP_DIR-on-localinstall.patch
Patch22: 0022-zypp-Implement-single-repo-refresh-feature.patch
Patch23: 0023-Validate-RPM-arch-before-local-install.-Fixes-JB-156.patch
Patch24: 0024-Clear-metadata-when-disabling-repositories.-JB-15874.patch
Patch25: 0025-Handle-and-log-C-exceptions-in-all-threads.patch
Patch26: 0026-Allow-scheduled-rebuilddb-runs-on-next-boot.patch
Patch27: 0027-Allow-cancelling-of-downloads.patch
Patch28: 0028-Also-abort-refresh-when-job-is-cancelled.patch
Patch29: 0029-Allow-searching-for-capabilities.patch
Patch30: 0030-Report-distro-upgrade-size-in-custom-request.patch
Patch31: 0031-Fix-download-size-calculation-prepare-for-cache-size.patch
Patch32: 0032-Separate-dist-upgrade-cache-directory-from-main-cach.patch
Patch33: 0033-Force-an-implicit-cache-refresh-before-checking-the-.patch
Patch34: 0034-make-sure-that-the-custom-config-is-set-for-synchron.patch
Patch35: 0035-Fixed-implementation-of-finding-newest-package-while.patch
Patch36: 0036-Revert-dependency-on-libzypp-version-14-as-we-cannot.patch
Patch37: 0037-PK_FILTER_ENUM_ARCH-_NOT_ARCH-to-filter-based-on-com.patch
Patch38: 0038-Downgrade-Glib-dependency.patch

Requires: PackageKit-zypp = %{version}-%{release}
Requires: shared-mime-info

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

Obsoletes: PackageKit-python
Obsoletes: PackageKit-debug-install
Obsoletes: PackageKit-plugin-devel

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
Requires: %{name} = %{version}-%{release}

%description glib
GLib libraries for accessing PackageKit.

%package glib-devel
Summary: GLib Libraries and headers for PackageKit
License: LGPLv2+
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: sqlite-devel
Requires: PackageKit-glib = %{version}-%{release}

%description glib-devel
GLib headers and libraries for PackageKit.


%package command-not-found
Summary: Ask the user to install command line programs automatically
Group: System/Libraries
Requires: bash
Requires: PackageKit-glib = %{version}-%{release}

%description command-not-found
A simple helper that offers to install new packages on the command line
using PackageKit.

%prep
%setup -q -n %{name}-%{version}/upstream
%patch1 -p1
%patch2 -p1
# This one can be removed when libzypp is upgraded
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
# This one can be removed when libzypp is upgraded
%patch37 -p1
%patch38 -p1


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
        --program-prefix= --prefix=/usr \
        --exec-prefix=/usr \
        --bindir=/usr/bin \
        --sbindir=/usr/sbin \
        --sysconfdir=/etc \
        --datadir=/usr/share \
        --includedir=/usr/include \
        --libdir=/usr/lib \
        --libexecdir=/usr/libexec \
        --localstatedir=/var \
        --sharedstatedir=/var/lib \
        --disable-static \
        --disable-dummy \
        --disable-cron \
        --enable-zypp \
        --with-default-backend=zypp \
        --enable-mce \
        --disable-local \
        --disable-strict \
        --disable-networkmanager \
        --disable-gstreamer-plugin \
        --enable-introspection=no \
        --enable-systemd \
        --disable-man-pages \
        --disable-tests \
        --disable-device-rebind \
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
%doc COPYING
%dir %{_datadir}/PackageKit
%dir %{_datadir}/PackageKit/helpers
%dir %{_sysconfdir}/PackageKit
%dir %{_localstatedir}/lib/PackageKit
%dir %{_localstatedir}/cache/PackageKit
%dir %{_localstatedir}/cache/PackageKit/downloads
%dir %{_libdir}/packagekit-backend
%config(noreplace) %{_sysconfdir}/PackageKit/*.conf
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
/lib/systemd/system/packagekit-offline-update.service
/lib/systemd/system/packagekit.service
/lib/systemd/system/system-update.target.wants/packagekit-offline-update.service
%{_libexecdir}/pk-offline-update
%{_libexecdir}/packagekit-direct

%files docs
%defattr(-,root,root,-)
%doc README AUTHORS  COPYING
#%{_mandir}/man1/*

%files zypp
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/packagekit-backend/libpk_backend_zypp.so
%{_libexecdir}/pk-rpm-db-clean
%{_unitdir}/rpm-db-clean.service
%config %{_sysconfdir}/zypp/packagekit-zypp-override.conf

%files glib
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*packagekit-glib*.so.*

%files command-not-found
%defattr(-,root,root,-)
%doc COPYING
%{_sysconfdir}/profile.d/*
%{_libexecdir}/pk-command-not-found
%config(noreplace) %{_sysconfdir}/PackageKit/CommandNotFound.conf

%files glib-devel
%defattr(-,root,root,-)
%doc README AUTHORS  COPYING
%{_libdir}/libpackagekit-glib*.so
%{_libdir}/pkgconfig/packagekit-glib2.pc
%dir %{_includedir}/PackageKit
%dir %{_includedir}/PackageKit/packagekit-glib2
%{_includedir}/PackageKit/packagekit-glib*/*.h

