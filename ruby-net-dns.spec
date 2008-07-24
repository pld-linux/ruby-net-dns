Summary:	Ruby library which implements a DNS resolver, a server and many other utilities
Name:		ruby-net-dns
Version:	0.4
Release:	0.1
License:	MIT
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/20677/net-dns-%{version}.tgz
# Source0-md5:	22182e53c8db20430dbed683596f38eb
URL:		http://net-dns.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
#BuildArch:	noarch
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# not noarch only due ruby packaging
%define		_enable_debug_packages	0

%description
Net::DNS is a pure Ruby library which implements a DNS resolver, a
server and many other utilities. The resolver allows the programmer to
perform nearly any type of DNS query from a Ruby script.

%prep
%setup -q -n net-dns-%{version}

%build
cp %{_datadir}/setup.rb .
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}
ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc AUTHORS CHANGELOG README THANKS
%dir %{ruby_rubylibdir}/net/dns
%{ruby_rubylibdir}/net/dns/dns.rb
%{ruby_rubylibdir}/net/dns/header.rb
%dir %{ruby_rubylibdir}/net/dns/names
%{ruby_rubylibdir}/net/dns/names/names.rb
%{ruby_rubylibdir}/net/dns/packet.rb
%{ruby_rubylibdir}/net/dns/question.rb
%{ruby_rubylibdir}/net/dns/resolver.rb
%dir %{ruby_rubylibdir}/net/dns/resolver
%{ruby_rubylibdir}/net/dns/resolver/socks.rb
%{ruby_rubylibdir}/net/dns/resolver/timeouts.rb
%{ruby_rubylibdir}/net/dns/rr.rb
%dir %{ruby_rubylibdir}/net/dns/rr
%{ruby_rubylibdir}/net/dns/rr/a.rb
%{ruby_rubylibdir}/net/dns/rr/aaaa.rb
%{ruby_rubylibdir}/net/dns/rr/classes.rb
%{ruby_rubylibdir}/net/dns/rr/cname.rb
%{ruby_rubylibdir}/net/dns/rr/hinfo.rb
%{ruby_rubylibdir}/net/dns/rr/mr.rb
%{ruby_rubylibdir}/net/dns/rr/mx.rb
%{ruby_rubylibdir}/net/dns/rr/ns.rb
%{ruby_rubylibdir}/net/dns/rr/null.rb
%{ruby_rubylibdir}/net/dns/rr/ptr.rb
%{ruby_rubylibdir}/net/dns/rr/soa.rb
%{ruby_rubylibdir}/net/dns/rr/srv.rb
%{ruby_rubylibdir}/net/dns/rr/txt.rb
%{ruby_rubylibdir}/net/dns/rr/types.rb
