#!/usr/bin/bash
network_interface=${1:-'eth0'}
output_file=${2:-'network_report.log'}

# Call fungsi ctrl_c kalau menerima SIGINT
trap ctrl_c SIGINT

function ctrl_c(){
    # Tulis filenya kemana
    printf "\rOutput written at %s\n" $output_file
}


sar -n DEV 1 1 | grep IFACE | tail -n 1 | sed 's/Average:/Time    /g' | tee /dev/tty > $output_file
sar -n DEV 1 | grep --line-buffered $network_interface | tee /dev/tty >> $output_file
