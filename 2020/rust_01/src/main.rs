use std::fs;
fn main() {
    let file_contents = fs::read_to_string("/Users/lunaferraraccio/Desktop/lille/advent_of_code/2020/rust_01/src/input")
        .expect("LogRocket: Should have been able to read the file");
//    println!("info.txt context =\n{file_contents}");

    // là j’ai arrêté de parser le fichier

    for first in file_contents.lines() {
        let first: i32 = first.parse().unwrap(); // a la place je parse ici
        for second in file_contents.lines() {
            let second: i32 = second.parse().unwrap(); // et là
            for third in file_contents.lines() {
                let third: i32 = third.parse().unwrap();
                if first + second + third == 2020 {
                    println!("{}", first * second * third)
                }
            }
            
        }
    }
}