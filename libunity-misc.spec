%define major	4
%define libname	%mklibname	unity-misc %{major}
%define develname	%mklibname	unity-misc -d

Name:           libunity-misc
Version:        4.0.4
Release:        1
License:        GPLv2,LGPLv2.1
Summary:        Miscellaneous differently licensed stuff for Unity
Url:            http://launchpad.net/libunity-misc
Group:          System/Libraries
Source0:        %{name}-%{version}.tar.gz
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
%configure2_5x \
   --disable-static
%make LIBS='-lm'

%install
%makeinstall_std
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

