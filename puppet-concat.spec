%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-concat
%global commit 5b86b60b4b3790a035cec11cb5052a15ea15a94d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-concat
Version:        7.1.1
Release:        1%{?alphatag}%{?dist}
Summary:        Construct files from multiple fragments.
License:        ASL 2.0

URL:            https://github.com/puppetlabs/puppetlabs-concat

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Construct files from multiple fragments.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/concat/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/concat/



%files
%{_datadir}/openstack-puppet/modules/concat/


%changelog
* Mon Sep 27 2021 RDO <dev@lists.rdoproject.org> 7.1.1-1.5b86b60git
- Update to post 7.1.1 (5b86b60b4b3790a035cec11cb5052a15ea15a94d)

