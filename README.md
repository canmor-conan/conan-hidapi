# conan-hidapi

conan-hidapi is a conan package for [signal11/hidapi](https://github.com/signal11/hidapi).

## Package Status

| Bintray | Windows | Linux & macOS |
|:--------:|:---------:|:-----------------:|
|[ ![Download](https://api.bintray.com/packages/canmor/conan/hidapi%3Acanmor/images/download.svg) ](https://bintray.com/canmor/conan/hidapi%3Acanmor/_latestVersion)|[![Build status](https://ci.appveyor.com/api/projects/status/6w6vl7a4vcnqrjo4?svg=true)](https://ci.appveyor.com/project/canmor/conan-hidapi)|[![Build Status](https://travis-ci.org/canmor/conan-hidapi.svg?branch=master)](https://travis-ci.org/canmor/conan-hidapi)|

## Conan.io Information

This packages can be found in the my personal Conan repository:

[Conan Repository on Bintray](https://bintray.com/canmor/conan)

*Note: You can click the "Set Me Up" button on the Bintray page above for instructions on using packages from this repository.*

## Known Issues

* This package version is named `latest` and pointed to HEAD of master branch, which might move up-to-date in future and broken your use.

    The latest release tag is 0.8 which was tagged at 2013, there're some critical bugs on that version such as crash on macOS, I can not figure out a release tag version to use.

* Not support x64 for Windows

    [signal11/hidapi](https://github.com/signal11/hidapi) provides a `sln` file to build for Windows, which lack support x64.

* Did not get a real usage test on Linux yet

If you get an idea to solve one of this issues, please report here or fork.
