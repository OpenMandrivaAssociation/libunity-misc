%define major	4
%define libname	%mklibname	unity-misc %{major}
%define develname	%mklibname	unity-misc -d

Name:           libunity-misc
Version:        4.0.4
Release:        3
License:        GPLv2,LGPLv2.1
Summary:        Miscellaneous differently licensed stuff for Unity
Url:            https://launchpad.net/libunity-misc
Group:          System/Libraries
Source0:        https://launchpad.net/libunity-misc/trunk/%{version}/+download/libunity-misc-%{version}.tar.gz
Patch0:			libunity-misc-4.0.4_werror.patch
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  gtk-doc

%description
This package provides miscellaneous stuff for Unity under several
licenses.

%package -n %{libname}
Summary:        Miscellaneous differently licensed stuff for Unity
Group:          System/Libraries

%description -n %{libname}
This package provides miscellaneous stuff for Unity under several
licenses.

%package -n %{develname}
Summary:        Development files for libunity-misc
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:		%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files for miscellaneous stuff used in Unity under several
licenses.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fi
%configure \
   --disable-static
%make_build LIBS='-lm'

%install
%make_install
find %{buildroot}%{_libdir} -name "*.la" -type f -print -delete


%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/unity-misc/
%{_libdir}/*.so
%{_libdir}/pkgconfig/unity-misc.pc
%{_datadir}/gtk-doc/html/%{name}/



%changelog
* Tue Nov 01 2011 Matthew Dawkins <mattydaw@mandriva.org> 4.0.4-1
+ Revision: 708238
- imported package libunity-misc


* Mon Oct 31 2011 Matthew Dawkins <mdawkins@unity-linux.org> 4.0.4-1-unity2011
- import for Unity
