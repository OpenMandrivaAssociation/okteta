Summary:	A simple HEX editor for KDE
Name:		okteta
Version:	4.14.3
Release:	2
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
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(qca2)
Conflicts:	kdesdk4-core < 1:4.11.0

%description
Okteta is a simple editor for the raw data of files. This type of program
is also called hex editor or binary editor.

%files
%doc %{_kde_docdir}/HTML/en/okteta
%{_kde_applicationsdir}/okteta.desktop
%{_kde_appsdir}/okteta
%{_kde_appsdir}/oktetapart
%{_kde_bindir}/okteta
%{_kde_bindir}/struct2osd.sh
%{_kde_configdir}/okteta-structures.knsrc
%{_kde_datadir}/appdata/okteta.appdata.xml
%{_kde_datadir}/config.kcfg/structviewpreferences.kcfg
%{_kde_datadir}/mime/packages/okteta.xml
%{_kde_iconsdir}/*/*/apps/okteta.png
%{_kde_libdir}/kde4/libkbytearrayedit.so
%{_kde_libdir}/kde4/oktetapart.so
%{_kde_services}/kbytearrayedit.desktop
%{_kde_services}/oktetapart.desktop

#----------------------------------------------------------------------------

%define kasten2controllers_major 2
%define libkasten2controllers %mklibname kasten2controllers %{kasten2controllers_major}

%package -n %{libkasten2controllers}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1controllers 0} < 1:4.10.0

%description -n %{libkasten2controllers}
Okteta shared library.

%files -n %{libkasten2controllers}
%{_kde_libdir}/libkasten2controllers.so.%{kasten2controllers_major}
%{_kde_libdir}/libkasten2controllers.so.0.*

#----------------------------------------------------------------------------

%define kasten2core_major 2
%define libkasten2core %mklibname kasten2core %{kasten2core_major}

%package -n %{libkasten2core}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1core 0} < 1:4.10.0

%description -n %{libkasten2core}
Okteta shared library.

%files -n %{libkasten2core}
%{_kde_libdir}/libkasten2core.so.%{kasten2core_major}
%{_kde_libdir}/libkasten2core.so.0.*

#----------------------------------------------------------------------------

%define kasten2gui_major 2
%define libkasten2gui %mklibname kasten2gui %{kasten2gui_major}

%package -n %{libkasten2gui}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1gui 0} < 1:4.10.0

%description -n %{libkasten2gui}
Okteta shared library.

%files -n %{libkasten2gui}
%{_kde_libdir}/libkasten2gui.so.%{kasten2gui_major}
%{_kde_libdir}/libkasten2gui.so.0.*

#----------------------------------------------------------------------------

%define kasten2okteta1controllers_major 1
%define libkasten2okteta1controllers %mklibname kasten2okteta1controllers %{kasten2okteta1controllers_major}

%package -n %{libkasten2okteta1controllers}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1okteta1controllers 0} < 1:4.10.0

%description -n %{libkasten2okteta1controllers}
Okteta shared library.

%files -n %{libkasten2okteta1controllers}
%{_kde_libdir}/libkasten2okteta1controllers.so.%{kasten2okteta1controllers_major}
%{_kde_libdir}/libkasten2okteta1controllers.so.0.*

#----------------------------------------------------------------------------

%define kasten2okteta1core_major 1
%define libkasten2okteta1core %mklibname kasten2okteta1core %{kasten2okteta1core_major}

%package -n %{libkasten2okteta1core}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1okteta1core 0} < 1:4.10.0

%description -n %{libkasten2okteta1core}
Okteta shared library.

%files -n %{libkasten2okteta1core}
%{_kde_libdir}/libkasten2okteta1core.so.%{kasten2okteta1core_major}
%{_kde_libdir}/libkasten2okteta1core.so.0.*

#----------------------------------------------------------------------------

%define kasten2okteta1gui_major 1
%define libkasten2okteta1gui %mklibname kasten2okteta1gui %{kasten2okteta1gui_major}

%package -n %{libkasten2okteta1gui}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname kasten1okteta1gui 0} < 1:4.10.0

%description -n %{libkasten2okteta1gui}
Okteta shared library.

%files -n %{libkasten2okteta1gui}
%{_kde_libdir}/libkasten2okteta1gui.so.%{kasten2okteta1gui_major}
%{_kde_libdir}/libkasten2okteta1gui.so.0.*

#----------------------------------------------------------------------------

%define okteta1core_major 1
%define libokteta1core %mklibname okteta1core %{okteta1core_major}

%package -n %{libokteta1core}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname okteta1core 0} < 1:4.10.0

%description -n %{libokteta1core}
Okteta shared library.

%files -n %{libokteta1core}
%{_kde_libdir}/libokteta1core.so.%{okteta1core_major}
%{_kde_libdir}/libokteta1core.so.0.*

#----------------------------------------------------------------------------

%define okteta1gui_major 1
%define libokteta1gui %mklibname okteta1gui %{okteta1gui_major}

%package -n %{libokteta1gui}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname okteta1gui 0} < 1:4.10.0

%description -n %{libokteta1gui}
Okteta shared library.

%files -n %{libokteta1gui}
%{_kde_libdir}/libokteta1gui.so.%{okteta1gui_major}
%{_kde_libdir}/libokteta1gui.so.0.*

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for Okteta
Group:		Development/KDE and Qt
Requires:	%{libkasten2controllers} = %{EVRD}
Requires:	%{libkasten2core} = %{EVRD}
Requires:	%{libkasten2gui} = %{EVRD}
Requires:	%{libkasten2okteta1controllers} = %{EVRD}
Requires:	%{libkasten2okteta1core} = %{EVRD}
Requires:	%{libkasten2okteta1gui} = %{EVRD}
Requires:	%{libokteta1core} = %{EVRD}
Requires:	%{libokteta1gui} = %{EVRD}

%description devel
This package includes the header files you will need to compile
applications that use Okteta libraries.

%files devel
%{_kde_includedir}/*
%{_kde_libdir}/libkasten2controllers.so
%{_kde_libdir}/libkasten2core.so
%{_kde_libdir}/libkasten2gui.so
%{_kde_libdir}/libkasten2okteta1controllers.so
%{_kde_libdir}/libkasten2okteta1core.so
%{_kde_libdir}/libkasten2okteta1gui.so
%{_kde_libdir}/libokteta1core.so
%{_kde_libdir}/libokteta1gui.so
%{_kde_libdir}/kde4/plugins/designer/oktetadesignerplugin.so

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.3-1
- New version 4.14.3

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.2-1
- New version 4.14.2
- Update files

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- Split from kdesdk4 package as upstream did
- New version 4.11.0
