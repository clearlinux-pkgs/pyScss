#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyScss
Version  : 1.3.5
Release  : 27
URL      : http://pypi.debian.net/pyScss/pyScss-1.3.5.tar.gz
Source0  : http://pypi.debian.net/pyScss/pyScss-1.3.5.tar.gz
Summary  : pyScss, a Scss compiler for Python
Group    : Development/Tools
License  : MIT
Requires: pyScss-bin
Requires: pyScss-python3
Requires: pyScss-license
Requires: pyScss-python
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pcre-dev
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six

%description
==================================
        
        |build-status| |coverage|

%package bin
Summary: bin components for the pyScss package.
Group: Binaries
Requires: pyScss-license

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
Requires: pyScss-python3
Provides: pyscss-python

%description python
python components for the pyScss package.


%package python3
Summary: python3 components for the pyScss package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyScss package.


%prep
%setup -q -n pyScss-1.3.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532526892
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose || : ; py.test-3.5 --verbose || : ;
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pyScss
cp LICENSE %{buildroot}/usr/share/doc/pyScss/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
%defattr(-,root,root,-)
/usr/share/doc/pyScss/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
