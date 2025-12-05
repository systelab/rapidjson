from conan import ConanFile
from conan.tools.files import copy, collect_libs, get
from conan.tools.microsoft import MSBuildDeps, MSBuildToolchain
import os

class RapidjsonConan(ConanFile):
    name = "rapidjson"
    description = "A fast JSON parser/generator for C++ with both SAX/DOM style API"
    homepage = "http://rapidjson.org/"
    url = "https://github.com/systelab/rapidjson"
    author = "CSW <csw@werfen.com>"
    license = "MIT"
    exports = ["LICENSE.md"]
    no_copy_source = True
    _source_subfolder = "source_subfolder"
    package_type = "header-library"

    def package(self):
        source_archive_url = "{0}/archive/v{1}.tar.gz".format(self.url, self.version)
        self.output.info(("Downloading sources from '%s'...") % source_archive_url)
        get(self, url=source_archive_url)
        
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

        include_folder = os.path.join(self.source_folder, "int", self._source_subfolder, "include")
        
        copy(self, pattern="license.txt", dst=os.path.join(self.package_folder, "licenses"), src=self._source_subfolder)
        copy(self, pattern="*", dst=os.path.join(self.package_folder, "include"), src=include_folder)
