from __future__ import print_function

from ctypes import CFUNCTYPE, c_int

import llvmlite.binding as llvm

import sys


# All these initializations are required for code generation!
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()  # yes, even this one

llvm.load_library_permanently("C:\\Windows\\System32\\msvcrt.dll")

def create_execution_engine():
    """
    Create an ExecutionEngine suitable for JIT code generation on
    the host CPU.  The engine is reusable for an arbitrary number of
    modules.
    """
    # Create a target machine representing the host
    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    # And an execution engine with an empty backing module
    backing_mod = llvm.parse_assembly("")
    engine = llvm.create_mcjit_compiler(backing_mod, target_machine)
    return engine


def compile_ir(engine, llvm_ir):
    """
    Compile the LLVM IR string with the given engine.
    The compiled module object is returned.
    """
    # Create a LLVM module object from the IR
    mod = llvm.parse_assembly(llvm_ir)
    mod.verify()
    # Now add the module and make sure it is ready for execution
    engine.add_module(mod)
    engine.finalize_object()
    return mod


engine = create_execution_engine()

f = open(sys.argv[1])
full_ir = f.read()

mod = compile_ir(engine, full_ir)

main_type = CFUNCTYPE(c_int)
main_func = main_type(engine.get_function_address("main"))

ret = main_func()
print("Program exited with exit code %d\n" % ret)
