import pywasm
import wasi

def sha256(v): 
    # sha256(start address char* input, int size, output address cgar* output)
    wasimod = wasi.Wasi(['sha-export.wasm'])
    runtime = pywasm.load('sha-export.wasm', { 'wasi_snapshot_preview1': wasimod.imports() })

    # allocate memory for the input string
    input_size = len(v)
    input_ptr = runtime.exec('malloc', [input_size])
    memory = runtime.store.memory_list[0].data

    # copy the input string to the allocated memory
    memory[input_ptr:input_ptr+input_size] = v

    # allocate memory for the output string (assuming SHA256 output size is 32 bytes)
    output_ptr = runtime.exec('malloc', [32])

    runtime.exec('SHA256', [input_ptr, input_size, output_ptr])

    # get result from the allocated memory
    result = memory[output_ptr:output_ptr+32]
    print("result: ", bytes(result))

    return bytes(result)
