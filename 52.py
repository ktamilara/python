import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc=new Scanner(System.in);
		int c11=sc.nextInt();
		int b11=sc.nextInt();
		int c12=sc.nextInt();
		int b12=sc.nextInt();
		int c13=sc.nextInt();
		int b13=sc.nextInt();
		int c14=sc.nextInt();
		int b14=sc.nextInt();
		if(c11==c12&&c13==c14&&b11==b14&&b12==b13)
		{
			System.out.println("yes");
		}
		else
		{
			System.out.println("no");
		}
	}
}
