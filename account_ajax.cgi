#!/usr/bin/perl -w
use CGI;
use DBI;
my $cgi = new CGI;
my $account = $cgi->param('account');
$DB_user = 'root';
$DB_pwd = 'supreme';
$DB_name = 'wp_server';

$dbh = DBI->connect("dbi:mysql:database=$DB_name;",$DB_user,$DB_pwd) or die "Connect Error";
$SQL= "select account from user where account = '$account'";
print "\"$account\" ";

#print $cgi->header("text/html");
$selectRecord = $dbh->prepare($SQL);
$selectRecord->execute();
$ref = $selectRecord->fetchrow_hashref();
if($ref){
	print "It's used";
}else{	print "It's OK";
}
$dbh->disconnect();
