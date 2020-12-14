#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyScss
Version  : 1.3.7
Release  : 42
URL      : https://files.pythonhosted.org/packages/e6/0d/6b52a5211121b870cc0c4c908b689fd460630b01a9e501a534db78e67bad/pyScss-1.3.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/e6/0d/6b52a5211121b870cc0c4c908b689fd460630b01a9e501a534db78e67bad/pyScss-1.3.7.tar.gz
Summary  : pyScss, a Scss compiler for Python
Group    : Development/Tools
License  : MIT
Requires: pyScss-bin = %{version}-%{release}
Requires: pyScss-license = %{version}-%{release}
Requires: pyScss-python = %{version}-%{release}
Requires: pyScss-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pcre-dev
BuildRequires : python3-dev
BuildRequires : six

%description
==================================
        
        |build-status| |coverage|

%package bin
Summary: bin components for the pyScss package.
Group: Binaries
Requires: pyScss-license = %{version}-%{release}

%description bin
bin components for the pyScss package.


%package license
Summary: license components for the pyScss package.
Group: Default

%description license
license components for the pyScss package.


%package python
Summary: python components for the pyScss package.
Group: Default
Requires: pyScss-python3 = %{version}-%{release}
Provides: pyscss-python

%description python
python components for the pyScss package.


%package python3
Summary: python3 components for the pyScss package.
Group: Default
Requires: python3-core
Provides: pypi(pyscss)
Requires: pypi(six)

%description python3
python3 components for the pyScss package.


%prep
%setup -q -n pyScss-1.3.7
cd %{_builddir}/pyScss-1.3.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587403810
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose || : ; py.test-3.5 --verbose || : ;
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyScss
cp %{_builddir}/pyScss-1.3.7/LICENSE %{buildroot}/usr/share/package-licenses/pyScss/c313f5aad9597bd831180c4a772e4c292248b00d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/less2scss
/usr/bin/pyscss

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyScss/c313f5aad9597bd831180c4a772e4c292248b00d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
