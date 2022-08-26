#Gil Dobrovinsky gilx0029 08/26/22

$break_line = "\n\n\n"


puts "#$break_line Parsing .txt File\n"
#Parse .txt
File.open("./SystemIntegration_individual/Week1_Homework/message.txt", "r") do |f|
    f.each_line do |line|
        puts line
    end
end

puts "#$break_line Parsing .csv File\n"



File.open("./SystemIntegration_individual/Week1_Homework/aboutme.csv", "r") do |f|
    f.each_line do |line|
        puts line
    end
end

puts "#$break_line Parsing .json File\n"


File.open("./SystemIntegration_individual/Week1_Homework/aboutme.json", "r") do |f|
    f.each_line do |line|
        puts line
    end
end

puts $break_line
