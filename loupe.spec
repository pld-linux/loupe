# TODO: use gtk4-update-icon-cache
Summary:	GNOME image viewer
Summary(pl.UTF-8):	Przeglądarka obrazów dla GNOME
Name:		loupe
Version:	44.3
Release:	0.1
License:	GPL v3+
Group:		X11/Applications/Graphics
Source0:	https://download.gnome.org/sources/loupe/44/%{name}-%{version}.tar.xz
# Source0-md5:	06d933b55f4f0ab0dd7b397f3162320e
URL:		https://gitlab.gnome.org/GNOME/loupe
BuildRequires:	cargo
BuildRequires:	gtk4-devel >= 4.11.2
BuildRequires:	lcms2-devel >= 2.12.0
BuildRequires:	libadwaita-devel >= 1.4
BuildRequires:	libheif-devel >= 1.14.2
BuildRequires:	libgweather4-devel >= 4.0.0
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	rust
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.26
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	gtk4 >= 4.11.2
Requires:	lcms2 >= 2.12.0
Requires:	libadwaita >= 1.4
Requires:	libheif >= 1.14.2
Requires:	libgweather4 >= 4.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Loupe is an image viewer application written with GTK 4, Libadwaita
and Rust.

%description -l pl.UTF-8
Loupe to przeglądarka obrazów napisana z użyciem GTK 4, Libadwaita
oraz języka Rust.


%prep
%setup -q
#%patch0 -p1

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}.lang

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
%{_iconsdir}/scalable/apps/org.gnome.Loupe.svg
%{_iconsdir}/scalable/apps/org.gnome.Loupe.Devel.svg
%{_iconsdir}/symbolic/apps/org.gnome.Loupe-symbolic.svg