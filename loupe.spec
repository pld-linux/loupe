# TODO: use gtk4-update-icon-cache
Summary:	GNOME image viewer
Summary(pl.UTF-8):	Przeglądarka obrazów dla GNOME
Name:		loupe
Version:	45.3
Release:	1
License:	GPL v3+
Group:		X11/Applications/Graphics
Source0:	https://download.gnome.org/sources/loupe/45/%{name}-%{version}.tar.xz
# Source0-md5:	bfd5e246f89fed13d03c4fe96089187f
Patch0:		%{name}-x32.patch
URL:		https://gitlab.gnome.org/GNOME/loupe
BuildRequires:	cargo
BuildRequires:	gtk4-devel >= 4.12.0
BuildRequires:	lcms2-devel >= 2.12.0
BuildRequires:	libadwaita-devel >= 1.4
BuildRequires:	libgweather4-devel >= 4.0.0
BuildRequires:	libheif-devel >= 1.14.2
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	rpmbuild(macros) >= 2.004
BuildRequires:	rust
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.26
Requires(post,postun):	gtk-update-icon-cache
Requires:	gtk4 >= 4.12.0
Requires:	hicolor-icon-theme
Requires:	lcms2 >= 2.12.0
Requires:	libadwaita >= 1.4
Requires:	libgweather4 >= 4.0.0
Requires:	libheif >= 1.14.2
ExclusiveArch:	%{rust_arches}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# debugsource packages don't support rust (or require adding some flags to rust/cargo)
%define		_debugsource_packages	0

%description
Loupe is an image viewer application written with GTK 4, Libadwaita
and Rust.

%description -l pl.UTF-8
Loupe to przeglądarka obrazów napisana z użyciem GTK 4, Libadwaita
oraz języka Rust.

%prep
%setup -q
%ifarch x32
%patch0 -p1
%endif

%build
%ifarch x32
export PKG_CONFIG_ALLOW_CROSS=1
%endif
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ifarch x32
export PKG_CONFIG_ALLOW_CROSS=1
%endif
%ninja_install -C build

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_desktop_database
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/loupe
%{_datadir}/dbus-1/services/org.gnome.Loupe.service
%{_datadir}/metainfo/org.gnome.Loupe.metainfo.xml
%{_desktopdir}/org.gnome.Loupe.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Loupe.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Loupe.Devel.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Loupe-symbolic.svg
