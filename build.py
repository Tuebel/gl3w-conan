from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(
        username='tuebel', channel="testing", stable_channel="testing",
        gcc_versions=['7'], archs=['x86_64'])
    builder.add_common_builds()
    builder.run()
