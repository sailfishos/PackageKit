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
Patch1:  001-zyppsupport-noproxy-for-pkcon-and-zypp-backend.patch
Patch2:  002-Add-pattern-support.patch
Patch3:  003-zypp-backend-Implement-upgradesystem-like-zypper-dup.patch
Patch4:  004-Force-repo-refresh-in-pkbackendrefreshcache.patch
Patch5:  005-Use-zyppperformexecution-for-system-upgrades.patch
Patch6:  006-Do-not-consider-satisfied-patterns-installed.patch
Patch7:  007-zypp-Backend-With-minimal-upgrade-only-download-pack.patch
Patch8:  008-zypp-Backend-Keep-track-of-overall-upgrade-install-p.patch
Patch9:  009-zypp-Backend-Close-PackageKit-job-when-upgrade-fails.patch
Patch10: 010-zypp-Backend-Look-for-patterns-matching-distroId-and.patch
Patch11: 011-zypp-Backend-Download-progress-reporting.patch
Patch12: 012-Add-libzypp-authentication-report-handler.patch
Patch13: 013-pkcon-Remove-y-assignment-from-onlydownload.patch
Patch14: 014-backends-zypp-Log-messages-into-systemd-journal.patch
Patch15: 015-backends-zypp-Check-free-space-before-executing-tran.patch
Patch16: 016-backends-zypp-Free-space-calculation-now-in-64bit.patch
Patch17: 017-backends-zypp-Fix-double-free-in-libzypp-TmpLineWrit.patch
Patch18: 018-logging-Silence-logging-output-use-systemd-journal-d.patch
Patch19: 019-backends-zypp-Dont-count-patterns-in-progress-calcul.patch
Patch20: 020-backends-zypp-Force-failure-for-missing-ssuini.patch
Patch21: 021-backends-zypp-Report-progress-for-download-and-insta.patch
Patch22: 022-backends-zypp-Detect-RPM-database-corruption-for-ini.patch
Patch23: 023-refresh-Dont-resolve-URL-in-zyppischangeablemedia.patch
Patch24: 024-enums-Add-l10n-handler-for-missing-roles.patch
Patch25: 025-backends-Call-dbrecovery-in-case-an-rpm-db-corruptio.patch
Patch26: 026-backends-zypp-Really-really-refresh-when-force-is-se.patch
Patch27: 027-plugins-scandesktopfiles-Dont-scan-manually-installe.patch
Patch28: 028-pktransaction-Fix-memory-leak-when-running-plugins.patch
Patch29: 029-backends-zypp-Remove-old-leftover-PKTMPDIR-on-locali.patch
Patch30: 030-backends-zypp-Implement-singlerepo-refresh-feature.patch
Patch31: 031-mce-Add-support-for-CPU-keepalive-during-transaction.patch
Patch32: 032-mce-Support-for-reconnecting-to-mce-when-its-gone.patch
Patch33: 033-mce-Make-critical-sections-bigger-to-be-thread-safe.patch
Patch34: 034-transaction-Always-allow-from-setgid-privileged-JB14.patch
Patch35: 035-pkcon-Improve-progress-output-on-non80x25-terminals.patch
Patch36: 036-mce-Check-proxy-before-sending-keepalive-Fixes-JB155.patch
Patch37: 037-zypp-Validate-RPM-arch-before-localinstall-Fixes-JB1.patch
Patch38: 038-zypp-Fix-possible-memory-leaks-with-heapallocated-it.patch
Patch39: 039-transaction-Builtin-policy-and-whitelist-Contributes.patch
Patch40: 040-zypp-Clear-metadata-when-disabling-repositories-JB15.patch
Patch41: 041-mce-Forcestop-thread-when-finalizing-engine-Fixes-JB.patch
Patch42: 042-zypp-Handle-and-log-C-exceptions-in-all-threads.patch
Patch43: 043-zypp-Mark-job-as-finished-when-exception-occurs.patch
Patch45: 045-zypp-Allow-scheduled-rebuilddb-runs-on-next-boot.patch
Patch46: 046-zypp-accept-i486-packages--JB18558.patch
Patch47: 047-zypp-Allow-cancelling-of-downloads.patch
Patch48: 048-zypp-Also-abort-refresh-when-job-is-cancelled.patch
Patch49: 049-zypp-Allow-searching-for-capabilities.patch
Patch50: 050-transaction-Update-whitelisted-applications-binary-n.patch
Patch51: 051-zypp-Take-uninstalled-due-to-upgrade-packages-into-a.patch
Patch52: 052-Fix-SIGFPE-when-no-packages-are-installed.patch
Patch53: 053-zypp-Report-distro-upgrade-size-in-custom-request.patch
Patch54: 054-zypp-Update-arch-compatiblity-check-for-x86.patch
Patch55: 055-zypp-Fix-download-size-calculation-prepare-for-cache.patch
Patch56: 056-zypp-Separate-distupgrade-cache-directory-from-main-.patch
Patch57: 057-zypp-Force-an-implicit-cache-refresh-before-checking.patch
Patch58: 058-zypp-Move-distupgrade-cache-to--home--Fixes-JB29268.patch
Patch59: 059-zypp-Fixed-crash-of-packagekitd-if-zypp-is-locked-by.patch
Patch60: 060-zypp-make-sure-that-the-custom-config-is-set-for-syn.patch
Patch61: 061-zypp-Fixed-some-size-computations-Contributes-to-JB3.patch
Patch62: 062-zypp-Fixed-implementation-of-finding-newest-package-.patch
Patch63: 063-zypp-Revert-dependency-on-libzypp-version-14-as-we-c.patch
Patch64: 064-zypp-Do-not-let-space-requirement-become-negative-Co.patch
Patch65: 065-Suppress-gtkdoc-building.patch

Requires: PackageKit-zypp = %{version}-%{release}
Requires: shared-mime-info
Requires: connman

BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: dbus-devel  >= %{dbus_version}
BuildRequires: dbus-glib-devel >= %{dbus_glib_version}
BuildRequires: pam-devel
BuildRequires: sqlite-devel
BuildRequires: connman-devel
BuildRequires: polkit-devel >= %{policykit_version}
BuildRequires: libtool
BuildRequires: python-devel
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
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
# This one can be removed when libzypp is upgraded
%patch63 -p1
%patch64 -p1
%patch65 -p1


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

touch $RPM_BUILD_ROOT%{_localstatedir}/cache/PackageKit/groups.sqlite

# create a link that from the comps icons to PK, as PackageKit frontends
# cannot add /usr/share/pixmaps/comps to the icon search path as some distros
# do not use comps. Patching this in the frontend is not a good idea, as there
# are multiple frontends in multiple programming languages.
pushd ${RPM_BUILD_ROOT}%{_datadir}/PackageKit > /dev/null
ln -s ../pixmaps/comps icons
popd > /dev/null


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
%doc COPYING
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

%files debug-install
%defattr(-,root,root,-)
%doc README AUTHORS  COPYING
%{_bindir}/pk-debuginfo-install

%files command-not-found
%defattr(-,root,root,-)
%doc README AUTHORS  COPYING
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

%files plugin-devel
%defattr(-,root,root,-)
%doc README AUTHORS  COPYING
%dir %{_includedir}/PackageKit
%{_includedir}/PackageKit/plugin/*.h
%{_libdir}/pkgconfig/packagekit-plugin.pc
