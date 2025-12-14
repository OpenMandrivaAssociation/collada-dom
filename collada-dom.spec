Name:           collada-dom
Version:        2.5.0
Release:        3
Summary:        COLLADA Document Object Model Library
License:        MIT
URL:            http://www.collada.org
Source0:        https://github.com/rdiankov/collada-dom/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         https://patch-diff.githubusercontent.com/raw/rdiankov/collada-dom/pull/43.patch
Patch1:         https://patch-diff.githubusercontent.com/raw/rdiankov/collada-dom/pull/44.patch

BuildRequires:  make
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(liburiparser)
BuildRequires:  pkgconfig(zlib)

%description
COLLADA is a royalty-free XML schema that enables digital asset exchange
within the interactive 3D industry. The COLLADA Document Object Model
(COLLADA DOM) is an application programming interface (API) that provides
a C++ object representation of a COLLADA XML instance document.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{version}
rm -rf dom/external-libs
dos2unix README.rst
dos2unix licenses/dom_license_e.txt
dos2unix licenses/license_e.txt

# try fix build with boost 1.89
sed -i 's/\<system\>//' CMakeLists.txt


%build
%cmake -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON
%make_build


%install
%make_install -C build

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
mv $RPM_BUILD_ROOT%{_libdir}/cmake/collada_dom-* $RPM_BUILD_ROOT%{_libdir}/cmake/collada_dom


%files
%doc README.rst licenses/dom_license_e.txt licenses/license_e.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/collada_dom/
