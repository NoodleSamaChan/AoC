use std::fs;

fn main() {
    let file_contents = fs::read_to_string("/Users/lunaferraraccio/Desktop/lille/advent_of_code/2022/01/rust_02/src/input")
    .expect("LogRocket: Should have been able to read the file");

    let mut biggest_number: i32 = 0;
    let mut biggest_number_two: i32 = 0;
    let mut biggest_number_three: i32 = 0;
    let mut calories_per_elf: i32 = 0;
    let mut vec: Vec<i32> = Vec::new();


    for first in file_contents.lines() {
        if first != "" {
            let first: i32 = first.parse().unwrap();
            calories_per_elf = calories_per_elf + first;
            

        } else {
            vec.push(calories_per_elf);
            calories_per_elf = 0
        }
    }
    vec.push(calories_per_elf);

    biggest_number = *vec.iter().max().unwrap();
    vec.retain(|value| *value != biggest_number);
    biggest_number_two = *vec.iter().max().unwrap();
    vec.retain(|value| *value != biggest_number_two);
    biggest_number_three = *vec.iter().max().unwrap();

    println!("{}", (biggest_number + biggest_number_two + biggest_number_three))
}