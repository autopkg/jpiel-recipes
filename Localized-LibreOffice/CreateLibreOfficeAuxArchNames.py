from autopkglib import Processor, ProcessorError

__all__ = ["CreateLibreOfficeAuxArchNames"]


class CreateLibreOfficeAuxArchNames(Processor):
    """This processor provides the extra architecture name needed for LibreOffice download paths for x86_64 and to use it in munki recipes."""
	
    input_variables = {
        "arch_name": {
            "required": True,
            "description": "The name of the architecture used in the source DMG and the output PKG.",
        }
    }
    output_variables = {
        "aux_arch_name": {"description": "The second form of architecture name used in the download path for x86_64.",}
    }

    description = __doc__

    def main(self):
        if ( self.env["arch_name"] ==  'aarch64'):
            # this architecture name is used consistently
            self.env["aux_arch_name"] = 'aarch64';
            self.env["munki_arch_name"] = 'arm64';
        elif ( self.env["arch_name"] == 'x86_64' ):
            # for x86_64 they use both forms in the path :(
            self.env["aux_arch_name"] = 'x86-64';
            self.env["munki_arch_name"] = 'x86_64';
        else:
            self.env["aux_arch_name"] = 'Architecture_' + arch_name + '_not_supported_by_CreateLibreOfficeAuxArchNames.';
            self.env["munki_arch_name"] = 'Architecture_' + arch_name + '_not_supported_by_CreateLibreOfficeAuxArchNames.';
if __name__ == "__main__":
    PROCESSOR = CreateLibreOfficeAuxArchNames()
    PROCESSOR.execute_shell()
    