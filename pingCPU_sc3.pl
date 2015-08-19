#!/usr/bin/perl
use strict;

#my @pktSize = (68,1280,1500,4352,7981,9198);
my @pktSize = (9198);
#my $ip = "192.168.10.10";
my $ip = "10.0.0.3";

foreach my $size(@pktSize){
    #open(FH, ">$size.txt") or die("couldnt open $size.txt");
    #my $endTime = time() + 20;
    #my $count = 0;

    my $ping = "ping -i 0.05 -w 30 -s $size -q $ip";
    #my $result = qx($ping);
    #print $result;
    #$count++;
    
    #print FH "number of packets: $count\n";
    #print FH "Ping summery result: $result\n";
    #close(FH);
}