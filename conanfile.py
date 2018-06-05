from conans import ConanFile, CMake, AutoToolsBuildEnvironment, tools


class HidapiConan(ConanFile):
    name = "hidapi"
    version = "latest"
    license = "GPL3"
    url = "https://github.com/canmor/conan-hidapi"
    description = "conan package for signal11/hidapi"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "minosx": ['10.7', '10.8', '10.9', '10.10', '10.11']
    }
    default_options = "minosx=10.7"
    generators = "cmake"
    source_dir = "hidapi-master"

    def config_options(self):
        if self.settings.os != "Macos":
            self.options.remove('minosx')

    def source(self):
        tools.download("https://github.com/signal11/hidapi/archive/master.zip", "hidapi.zip")
        tools.unzip("hidapi.zip")
        if self.settings.os != "Windows":
            self.run("chmod +x ./%s/bootstrap" % self.source_dir)

    def build(self):
        if self.settings.os == "Windows":
            if self.settings.compiler == "Visual Studio":
                self.build_msvc()
        else:
            self.build_unix()

    def build_msvc(self):
         msbuild = MSBuild(self)
         msbuild.build("windows/hidapi.sln")

    def build_unix(self):
        args = ["-prefix %s" % self.package_folder]
        self.run("cd %s && ./bootstrap" % self.source_dir)
        autotools = AutoToolsBuildEnvironment(self)
        if self.settings.os == "Macos":
            autotools.flags.append('-mmacosx-version-min=%s' % self.options.minosx)
        autotools.configure(self.source_dir)
        autotools.make()
        autotools.install()

    def package(self):
        self.copy("*.h", dst="include", src="hidapi")
        self.copy("*hidapi.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        if self.settings.os == "Linux":
            self.cpp_info.libs = ["hidapi-libusb"]
        else:
            self.cpp_info.libs = ["hidapi"]

