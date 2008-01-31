%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	HL7
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - HL7 messaging API
Summary(pl.UTF-8):	%{_pearname} - API wysyłania wiadomości HL7
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	4
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	9a811c807cadbf7fcad9675aedd3155e
URL:		http://pear.php.net/package/Net_HL7/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an HL7 API for creating, sending and
manipulating HL7 messages. HL7 is a protocol on the 7th OSI layer
(hence the '7' in HL7) for messaging in Health Care environments. HL7
means 'Health Level 7'. HL7 is a protocol with a wealth of semantics
that defines hundreds of different messages and their meaning, but
also defines the syntactics of composing and sending messages. The API
is focused on the syntactic level of HL7, so as to remain as flexible
as possible. The package is a translation of the Perl HL7 Toolkit and
will be kept in sync with this initiative.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza API HL7 do tworzenia, wysyłania i obróbki
komunikatów HL7. HL7 to protokół w 7 warstwie OSI (stąd '7' w HL7) do
komunikacji w środowiskach Health Care. HL7 oznacza "Health Level 7'.
HL7 to protokół z bogatą semantyką definiujący setki różnych
komunikatów i ich znaczenia, ale także definiujący składnię tworzenia
i wysyłania komunikatów. API skupia się na poziomie składni HL7, tak,
aby pozostać jak najbardziej elastycznym. Pakiet jest tłumaczeniem
perlowego zestawu narzędzi HL7 i będzie utrzymywany w synchronizacji z
tą inicjatywą.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/README
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
