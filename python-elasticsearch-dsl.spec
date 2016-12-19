# Created by pyp2rpm-3.2.1
%global pypi_name elasticsearch-dsl

Name:           python-%{pypi_name}
Version:        5.0.0
Release:        1%{?dist}
Summary:        Python client for Elasticsearch

License:        Apache License, Version 2.0
URL:            https://github.com/elasticsearch/elasticsearch-dsl-py
Source0:        https://files.pythonhosted.org/packages/source/e/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-mock
#BuildRequires:  python-pytest
#BuildRequires:  python-pytest-cov
BuildRequires:  python-pytz
BuildRequires:  python-unittest2
BuildRequires:  python-setuptools

%description
Elasticsearch DSL Elasticsearch DSL is a highlevel library whose aim is to help
with writing and running queries against Elasticsearch. It is built on top of
the official lowlevel client (elasticsearchpy < provides a more convenient and
idiomatic way to write and manipulate queries. It stays close to the
Elasticsearch JSON DSL, mirroring its terminology and structure. It exposes the
whole ...

%package -n     python2-%{pypi_name}
Summary:        Python client for Elasticsearch
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-six
Requires:       python-dateutil
Requires:       python-elasticsearch >= 5.0.0
Requires:       python-elasticsearch < 6.0.0
%description -n python2-%{pypi_name}
Elasticsearch DSL Elasticsearch DSL is a highlevel library whose aim is to help
with writing and running queries against Elasticsearch. It is built on top of
the official lowlevel client (elasticsearchpy < provides a more convenient and
idiomatic way to write and manipulate queries. It stays close to the
Elasticsearch JSON DSL, mirroring its terminology and structure. It exposes the
whole ...


%prep
%autosetup -n %{name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
%py2_install


#%check
#%{__python2} setup.py test

%files -n python2-%{pypi_name}
%doc 
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/elasticsearch_dsl-%{version}-py?.?.egg-info

%changelog
* Mon Dec 19 2016 John Doe <john@doe.com> - 5.0.0-1
- Initial package.
