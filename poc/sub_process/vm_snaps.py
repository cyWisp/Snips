#!/usr/bin/env python
from subprocess import Popen, PIPE
from sys import argv, exit

def execute(c_list):
	command = Popen(
		c_list,
		stdout=PIPE,
		stderr=PIPE,
	)
	
	output = command.communicate()[0].decode("utf-8")
	error = command.communicate()[1].decode("utf-8")

	return output, error

def read_vm_list(file_name):
    try:
        with open(file_name, "r+") as vms:
            vm_list = [vm.strip("\n") for vm in vms.readlines()]
    except Exception as e:
        print(f"[x] Error reading vm list: {e}")
        exit()
    else: return vm_list
    finally: vms.close()

def get_snapshots(vm_list):
    
    snapshots_by_host = dict()

    for vm in vm_list:
        vmrun_list_command = ["vmrun", "listSnapshots", vm]
        output, error = execute(vmrun_list_command)

        if error != "":
            print("[x] Error: {error}")
            continue
        else: pass

        if output:
            node_name = vm.split("/")[-1]
            snapshots = list(output.split("\n"))
            
            for index, snapshot in enumerate(snapshots):
                if "Total" in snapshot:
                    del snapshots[index]
                else: continue
            
            snapshots_by_host[node_name] = snapshots
    
    return snapshots_by_host

    
        
if __name__ == '__main__':

    vm_list = read_vm_list(argv[1])
    node_snaps = get_snapshots(vm_list)

    for node_name, snapshot_list in node_snaps.items():
        print(f"{node_name}:\n")
        for snapshot in snapshot_list:
            print(snapshot)

