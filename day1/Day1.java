import java.io.*;
import java.util.*;

public class Day1 {

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new FileReader(new File(args[0])));
        //nested loop to check all elves and find sum for each elf
        ArrayList<Integer> sums = new ArrayList<Integer>();
        while(in.ready()) {
            String line = in.readLine();
            int sum = 0;
            while(line.length() > 0) {
                sum += Integer.parseInt(line);
                line = in.readLine();
            }            
            sums.add(sum);
        }
        Collections.sort(sums, Collections.reverseOrder());
        int total = 0;
        for(int i = 0; i < 3; i++) {
            total += sums.get(i);
        }
        System.out.println(total);
    }
}
