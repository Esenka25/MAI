#!/bin/bash
awk 'BEGIN{
print "____________________________________";
print "User | School number | Average mark";
m=0
w=0}
{
if ($2 == "Man")
{print $1 "\t " $3 "\t \t" $4;}
if ($2 == "Man") m++;
else if ($2 == "Woman") w++;
}END{
print "\n";
if (m > w) print "Most of users are Men ( " m " of " NR - 1 " )" ;
else print "Most of users are Women ( " w " of " NR - 1 " )";
}' lab20.txt
