%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	UML
%define		_status		beta
%define		_pearname	PHP_UML
Summary:	%{_pearname} - produce an UML/XMI representation of the classes and packages found on system
Summary(pl.UTF-8):	%{_pearname} - tworzenie struktury UML/XMI klas i pakietów znalezionych w systemie
Name:		php-pear-%{_pearname}
Version:	0.5.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	15507c3d92345946cc76e69adf889e24
URL:		http://pear.php.net/package/PHP_UML/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP_UML is a PHP parser, an XMI generator, as well as a
metamodel-driven application. Practically, with PHP_UML, you can feed
an UML CASE tool, like Rational Rose or Argouml, with an UML
representation of existing PHP source code. This way, you get an
instant overview of a given application, with all the usual functions
of a software design tool, like class diagrams exportation,
refactoring of object-oriented applications, or automatic code
generation.

PHP_UML:
 - Parses classes, interfaces, inheritance and implementation
   relations,
 - Parses properties, class constants, visibility and static
   attributes,
 - Parses functions, their parameters, their default values, their
   types (when stated),
 - Parses docblock comments : class comments (@package), function
   comments (@param and @return) and header file comments (@package),
 - Interprets the PHP namespacing instructions ("namespace" and "use"),
 - Does automatic type detection, through the default values,
 - Generates UML in version 1.4, and version 2.1,
 - Generates logical, component, and deployment views,

Other UML elements will be available in future releases.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
PHP_UML to parser PHP, generator XML jak również aplikacja wzorowana
na meta-model. Praktycznie rzecz biorąc, za pomocą PHP_UML możliwe
jest przekazanie narzędziom UML CASE, takim jak Rational Rose czy
Argouml, schematu UML kodu PHP. W ten sposób możliwe jest
natychmiastowy podgląd aplikacji, ze wszystkimi funkcjami narzędzi do
projektowania aplikacjia, takimi jak eksportem diagramów funkcji,
refaktoryzacji zorientowanych obiektowo aplikacji, czy automatycznego
generowania kodu.

PHP_UML:
 - przetwarzanie relacji klas, interfejsów, dziedziczenia i
   implementacji,
 - przetwarzanie właściwości, stałych, widoczności i stałych atrybutów
   klas,
 - przetwarzanie funkcji, ich parametrów, zwracanych funkcji i typów
   (jeśli określone),
 - przetwarzanie komentarzy docblook : komentarzy klas (@package),
   funkcji (@param i @return) i nagłówków plików (@package),
 - interpretacja instrukcji przestrzeni nazw PHP ("namespace" i "use"),
 - autoamtyczna detekcja typu z pomocą domyślnych wartości,
 - generowania UML w wersji 1.4 i 2.1
 - generowanie widoków logicznych, komponentów.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
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
%doc install.log docs/PHP_UML/{docs,examples}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PHP/UML
%{php_pear_dir}/PHP/UML.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/PHP_UML
