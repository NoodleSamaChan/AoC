use std::fs;
fn main() {
    let file_contents = fs::read_to_string("/Users/lunaferraraccio/Desktop/lille/advent_of_code/2018/01/day_1/src/input")
    .expect("LogRocket: Should have been able to read the file");
    let mut counter:i32 = 0;

    for line in file_contents.lines() {
        let line:i32 = line.parse().unwrap();
        counter = counter + line;
    }

    println!("{}", counter);
}
