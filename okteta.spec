Summary:	A simple HEX editor for KDE
Name:		okteta
Version:	14.12.0
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(qca2)
BuildRequires:	extra-cmake-modules5
BuildRequires:	ninja
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Designer) qt5-designer

%description
Okteta is a simple editor for the raw data of files. This type of program
is also called hex editor or binary editor.

%files
%doc %{_kde_docdir}/HTML/en/okteta
%{_datadir}/applications/org.kde.okteta.desktop
%{_datadir}/okteta
%{_datadir}/oktetapart
%{_datadir}/kxmlgui5/okteta
%{_bindir}/okteta
%{_bindir}/struct2osd.sh
%{_sysconfdir}/xdg/okteta-structures.knsrc
%{_datadir}/appdata/okteta.appdata.xml
%{_datadir}/config.kcfg/structviewpreferences.kcfg
%{_datadir}/mime/packages/okteta.xml
%{_iconsdir}/*/*/apps/okteta.png
%{_libdir}/qt5/plugins/oktetapart.so

#----------------------------------------------------------------------------

%define kasten3controllers_major 3
%define libkasten3controllers %mklibname kasten3controllers %{kasten3controllers_major}

%package -n %{libkasten3controllers}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1controllers 0} < 1:4.10.0
Obsoletes:	%{mklibname kasten2controllers 0} < 1:14.12.0

%description -n %{libkasten3controllers}
Okteta shared library.

%files -n %{libkasten3controllers}
%{_kde_libdir}/libkasten3controllers.so.%{kasten3controllers_major}
%{_kde_libdir}/libkasten3controllers.so.0.*

#----------------------------------------------------------------------------

%define kasten3core_major 3
%define libkasten3core %mklibname kasten3core %{kasten3core_major}

%package -n %{libkasten3core}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1core 0} < 1:4.10.0
Obsoletes:	%{mklibname kasten2core 0} < 1:14.12.0

%description -n %{libkasten3core}
Okteta shared library.

%files -n %{libkasten3core}
%{_kde_libdir}/libkasten3core.so.%{kasten3core_major}
%{_kde_libdir}/libkasten3core.so.0.*

#----------------------------------------------------------------------------

%define kasten3gui_major 3
%define libkasten3gui %mklibname kasten3gui %{kasten3gui_major}

%package -n %{libkasten3gui}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1gui 0} < 1:4.10.0
Obsoletes:	%{mklibname kasten2gui 0} < 1:14.12.0

%description -n %{libkasten3gui}
Okteta shared library.

%files -n %{libkasten3gui}
%{_kde_libdir}/libkasten3gui.so.%{kasten3gui_major}
%{_kde_libdir}/libkasten3gui.so.0.*

#----------------------------------------------------------------------------

%define kasten3okteta1controllers_major 1
%define libkasten3okteta1controllers %mklibname kasten3okteta1controllers %{kasten3okteta1controllers_major}

%package -n %{libkasten3okteta1controllers}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1okteta1controllers 0} < 1:4.10.0
Obsoletes:	%{mklibname kasten2okteta1controllers 0} < 1:14.12.0

%description -n %{libkasten3okteta1controllers}
Okteta shared library.

%files -n %{libkasten3okteta1controllers}
%{_kde_libdir}/libkasten3okteta1controllers.so.%{kasten3okteta1controllers_major}
%{_kde_libdir}/libkasten3okteta1controllers.so.0.*

#----------------------------------------------------------------------------

%define kasten3okteta1core_major 1
%define libkasten3okteta1core %mklibname kasten3okteta1core %{kasten3okteta1core_major}

%package -n %{libkasten3okteta1core}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1okteta1core 0} < 1:4.10.0
Obsoletes:	%{mklibname kasten2okteta1core 0} < 1:14.12.0

%description -n %{libkasten3okteta1core}
Okteta shared library.

%files -n %{libkasten3okteta1core}
%{_kde_libdir}/libkasten3okteta1core.so.%{kasten3okteta1core_major}
%{_kde_libdir}/libkasten3okteta1core.so.0.*

#----------------------------------------------------------------------------

%define kasten3okteta1gui_major 1
%define libkasten3okteta1gui %mklibname kasten3okteta1gui %{kasten3okteta1gui_major}

%package -n %{libkasten3okteta1gui}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1okteta1gui 0} < 1:4.10.0
Obsoletes:	%{mklibname kasten2okteta1gui 0} < 1:14.12.0

%description -n %{libkasten3okteta1gui}
Okteta shared library.

%files -n %{libkasten3okteta1gui}
%{_kde_libdir}/libkasten3okteta1gui.so.%{kasten3okteta1gui_major}
%{_kde_libdir}/libkasten3okteta1gui.so.0.*

#----------------------------------------------------------------------------

%define okteta2core_major 2
%define libokteta2core %mklibname okteta2core %{okteta2core_major}

%package -n %{libokteta2core}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname okteta1core 0} < 1:4.10.0
Obsoletes:	%{mklibname okteta1core 1} < 1:14.12.0

%description -n %{libokteta2core}
Okteta shared library.

%files -n %{libokteta2core}
%{_kde_libdir}/libokteta2core.so.%{okteta2core_major}
%{_kde_libdir}/libokteta2core.so.0.*

#----------------------------------------------------------------------------

%define okteta2gui_major 2
%define libokteta2gui %mklibname okteta2gui %{okteta2gui_major}

%package -n %{libokteta2gui}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname okteta1gui 0} < 1:4.10.0
Obsoletes:	%{mklibname okteta1gui 1} < 1:14.12.0

%description -n %{libokteta2gui}
Okteta shared library.

%files -n %{libokteta2gui}
%{_kde_libdir}/libokteta2gui.so.%{okteta2gui_major}
%{_kde_libdir}/libokteta2gui.so.0.*

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for Okteta
Group:		Development/KDE and Qt
Requires:	%{libkasten3controllers} = %{EVRD}
Requires:	%{libkasten3core} = %{EVRD}
Requires:	%{libkasten3gui} = %{EVRD}
Requires:	%{libkasten3okteta1controllers} = %{EVRD}
Requires:	%{libkasten3okteta1core} = %{EVRD}
Requires:	%{libkasten3okteta1gui} = %{EVRD}
Requires:	%{libokteta2core} = %{EVRD}
Requires:	%{libokteta2gui} = %{EVRD}

%description devel
This package includes the header files you will need to compile
applications that use Okteta libraries.

%files devel
%{_includedir}/*
%{_libdir}/libkasten3controllers.so
%{_libdir}/libkasten3core.so
%{_libdir}/libkasten3gui.so
%{_libdir}/libkasten3okteta1controllers.so
%{_libdir}/libkasten3okteta1core.so
%{_libdir}/libkasten3okteta1gui.so
%{_libdir}/libokteta2core.so
%{_libdir}/libokteta2gui.so
%{_libdir}/qt5/plugins/designer/oktetadesignerplugin.so

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja install -C build
