# hashcat_rules_formatter
Formats hashcat rules files into a more readable format

```
syntax: python rulesformatter.py file
```

## Example:

input file:
```
:
E
@0@1@2@3@4@5@6@7@8@9$1$2$3
i5no6ei7ai8t
o1\x41o2\x42
@0@1@2@3@4@5@6@7@8@9$1
l$1$2
]$7
s9\s8~s79s68s57s46s35s24s13s02s\1s~0
```

output:
```
: 
E 
@0 @1 @2 @3 @4 @5 @6 @7 @8 @9 $1 $2 $3 
i5n o6e i7a i8t 
o1\x41o o2\x42 
@0 @1 @2 @3 @4 @5 @6 @7 @8 @9 $1 
l $1 $2 
] $7 
s9\ s8~ s79 s68 s57 s46 s35 s24 s13 s02 s\1 s~0
```
