#!/usr/local/bin/perl

use Data::Dumper;

my @momoclo = (
  '百田夏菜子',
  '玉井詩織',
  '佐々木彩夏',
  '有安杏果',
  '早見あかり'
);

print Dumper(\@momoclo);

pop(@momoclo);

print Dumper(\@momoclo);
