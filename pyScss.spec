#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyScss
Version  : 1.3.4
Release  : 16
URL      : https://pypi.python.org/packages/source/p/pyScss/pyScss-1.3.4.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pyScss/pyScss-1.3.4.tar.gz
Summary  : pyScss, a Scss compiler for Python
Group    : Development/Tools
License  : MIT
Requires: pyScss-bin
Requires: pyScss-python
BuildRequires : pbr
BuildRequires : pcre-dev
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six

%description
pyScss, a Scss compiler for Python
==================================
|build-status| |coverage|

%package bin
Summary: bin components for the pyScss package.
Group: Binaries

%description bin
bin components for the pyScss package.


%package python
Summary: python components for the pyScss package.
Group: Default
Provides: pyscss-python

%description python
python components for the pyScss package.


%prep
%setup -q -n pyScss-1.3.4

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
#py.test-2.7 --verbose; py.test-3.5 --verbose;
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyscss

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
