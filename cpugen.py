# cpugen.py
# Extracts the cpu's generation
# usage: cpugen.py file
# file: file containing cpu
import re
import sys
import argparse
import json

cpu_gen_pattern = r'[\s\w-]?(\d)[\d\w]+'


def get_cpu_gen(cpu_name):
    """
    Extracts cpu's generation from cpu name
    """
    cpu_name = cpu_name.replace('\n', '')
    match = re.findall(cpu_gen_pattern, cpu_name)
    if match:
        return match[-1]
    return None


description = "Extracts generation from cpu name"
usage = "cpugen.py [-f file | -n cpu_name ]"
examples="""
Examples:
cpugen.py -f cpulist.txt
cpugen.py -n "Intel Xeon E5-2430 v2"
"""
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=description,
    usage=usage,
    epilog=examples,
    prog='cpugen')

# optional arguments
parser.add_argument('-f','--file', metavar='', type=str, help='file with line separated list of cpu namese')
parser.add_argument('-n','--name', metavar='', type=str, help='cpu name')
parser.add_argument('-dj', '--dumpjson', metavar='', type=str, help='export to json')
# parser.add_argument('-h', '--help', metavar='', type=str, help='help')

args = parser.parse_args()

# if input filename was specified
if args.file:
    try:
        with open(args.file) as fh:
            # read all the cpu names into a list
            cpus = fh.readlines()

            # will hold list of dictionaries
            cpu_info = []

            # generate list of dictionaries
            # with cpu's name and generation
            for cpu in cpus:
                cpu_name = cpu.replace('\n', '')    
                gen = get_cpu_gen(cpu_name)
                cpu_info.append(
                    {
                        "cpu": cpu_name,
                        "generation": gen
                    }
                )
            
            # if jsondump outfile was specified
            if args.dumpjson:
                outfile = args.dumpjson
                with open(outfile, 'w') as outfh:
                    json.dump(cpu_info, outfh)
            # display to console if outfile is not specified
            else:
                for cpu in cpu_info:
                    print(f'cpu: {cpu["cpu"]} - generation: {cpu["generation"]}')

    except Exception as ex:
        print(f'Error: {str(ex)}')
    sys.exit(0)

if args.name:
    print(f'CPU: {args.name} - Generation: {get_cpu_gen(args.name)}')

