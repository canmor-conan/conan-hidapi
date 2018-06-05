from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    command = "sudo dpkg --add-architecture i386 && sudo apt-get update && sudo apt-get install -y libudev-dev libusb-1.0-0-dev libudev-dev:i386 libusb-1.0-0-dev:i386"
    builder = ConanMultiPackager(docker_entry_script=command)
    builder.add_common_builds()
    builder.run()
