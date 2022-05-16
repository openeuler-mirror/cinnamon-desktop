%global gtk3_version                      3.16.0
%global glib2_version                     2.37.3
%global startup_notification_version      0.5
%global gtk_doc_version                   1.9
%global po_package                        cinnamon-desktop-3.0

Name:    cinnamon-desktop
Version: 5.2.0
Release: 1
Summary: Shared code among cinnamon-session, nemo, etc
License: GPLv2+ and LGPLv2+ and MIT
URL:     https://github.com/linuxmint/%{name}
Source0: https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1: x-cinnamon-mimeapps.list
Patch0:  set_font_defaults.patch

ExcludeArch: %{ix86}

BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(libstartup-notification-1.0) >= %{startup_notification_version}
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires: pkgconfig(gtk-doc) >= %{gtk_doc_version}
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(accountsservice) 
BuildRequires: meson
BuildRequires: intltool
BuildRequires: itstool

Requires: redhat-menus
Requires: system-backgrounds-gnome
Requires: gnome-themes-standard

%description
The cinnamon-desktop package contains an internal library
(libcinnamon-desktop) used to implement some portions of the CINNAMON
desktop, and also some data files and other shared components of the
CINNAMON user environment.

%package devel
Summary:  Libraries and headers for libcinnamon-desktop
License:  LGPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}

Requires: gtk3-devel >= %{gtk3_version}
Requires: glib2-devel >= %{glib2_version}
Requires: startup-notification-devel >= %{startup_notification_version}

%description devel
Libraries and header files for the CINNAMON-internal private library
libcinnamon-desktop.

%prep
%autosetup -p1

%build
%meson -Dpnp_ids=/usr/share/hwdata/pnp.ids -Ddeprecation_warnings=false
%meson_build

%install
%meson_install

mkdir -p %buildroot%{_datadir}/applications/
install -m 644 %SOURCE1 %buildroot%{_datadir}/applications/x-cinnamon-mimeapps.list

%find_lang %{po_package} --all-name --with-gnome
%ldconfig_scriptlets

%files -f %{po_package}.lang
%doc AUTHORS README
%license COPYING COPYING.LIB
%{_datadir}/glib-2.0/schemas/org.cinnamon.*.xml
%{_datadir}/applications/x-cinnamon-mimeapps.list
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/C*.typelib

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/cinnamon-desktop/
%{_datadir}/gir-1.0/C*.gir

%changelog
* Fri May 6 2022 lin zhang <lin.zhang@turbolinux.com.cn> - 5.2.0-1
- Initial Packaging
