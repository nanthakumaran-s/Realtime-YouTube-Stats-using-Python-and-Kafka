#!/bin/bash

while getopts t: flag
do
    case "${flag}" in
        t) task=${OPTARG};;
    esac
done

python3 src/producer/producer.py $task