%define		_status		stable
%define		_pearname	PHP_UML
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - produce an UML/XMI representation of the classes and packages found on system
Summary(pl.UTF-8):	%{_pearname} - tworzenie struktury UML/XMI klas i pakietów znalezionych w systemie
Name:		php-pear-%{_pearname}
Version:	1.6.0
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a200a5f716527dd2bd75f4a988417841
URL:		http://pear.php.net/package/PHP_UML/
BuildRequires:	php-pear-PEAR >= 1:1.4.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(spl)
Requires:	php(xsl)
Requires:	php-pear
Requires:	php-pear-Console_CommandLine
Obsoletes:	php-pear-PHP_UML-tests
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
%{php_pear_dir}/data/PHP_UML
