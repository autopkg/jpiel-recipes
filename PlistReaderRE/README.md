# PlistReaderRE

PlistReaderRE was a try to add to PlistReader Processor the ability ro apply some string changes to values.

It is then clearly a fork of PlistReader processor where i tried to add support for re.sub().

In addition to the arguments of PlistReader, you can then add a new dictionnary named plist_regex.
For every key in plist_keys, you CAN have a corresponding dict in plist_regex that must contain a pattern key and a repl key.

Example :
```<key>plist_regex</key>
<dict>
        <key>CFBundleShortVersionString</key>
        <dict>
            <key>pattern</key>
            <string>.*</string>
            <key>repl</key>
            <string>\1</string>
         </dict>
</dict>```

As of now, it doesn't work because of the special chars in repl string.
