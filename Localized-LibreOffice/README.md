This package was inspired by Michal Moravec's work. Thanks to him !

His recipe was done to allow installation of differents languages packs for LibreOffice, as separate recipes from LibreOffice.
Since this caused some problems, i decided to go the other way. Instead of installing a separate laguage pack, i will do a localized version of LibreOffice.

The problem with my solution is that if you won't be able to install other language pack by this way. But in my usecase and i think in usecase of many others, it's not a problem.

I also simplified a lot the process, maybe because the parent recipe for LibreOffice was also simplified.

Localized-LibreOffice.download.recipe :
 - Use  io.github.hjuutilainen.download.LibreOffice as parent recipe to download the latest version of LibreOffice.
 - Download the language pack.
 - Mount the DMG of LibreOffice and copy the content in the Cache
 - Mount the DMG of LanguagePack and expand it in the LibreOffice application.
 
 Localized-LibreOffice.pkg.recipe :
 - package the merged LibreOffice application
 
Localized-LibreOffice.munki.recipe : 
- create the munki pkg
