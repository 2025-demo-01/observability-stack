from bcc import BPF 
program = """
int trace_sys_enter(void *ctx) { return 0; }
"""
b = BPF(text=program)
print("ebpf loaded")
