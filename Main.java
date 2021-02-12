package com.company;

import javax.swing.*;
import java.util.Scanner;

public class Main {
    public static final String ANSI_RESET = "\u001B[0m";
    public static final String ANSI_BLACK = "\u001B[30m";
    public static final String ANSI_RED = "\u001B[31m";
    public static final String ANSI_GREEN = "\u001B[32m";
    public static final String ANSI_YELLOW = "\u001B[33m";
    public static final String ANSI_BLUE = "\u001B[34m";
    public static final String ANSI_PURPLE = "\u001B[35m";
    public static final String ANSI_CYAN = "\u001B[36m";
    public static final String ANSI_WHITE = "\u001B[37m";

    public int depositTerm;
    public int depositPercent;

    static void depositTermUser() {
        System.out.println("*********************************************");
        System.out.println(ANSI_GREEN + "What the term of deposit you want to choose?" + ANSI_RESET);
        System.out.println(ANSI_GREEN + "1. 3 months" + ANSI_RESET);
        System.out.println(ANSI_GREEN + "2. 6 months" + ANSI_RESET);
        System.out.println(ANSI_GREEN + "3. 12 months" + ANSI_RESET);
        System.out.println(ANSI_GREEN + "Please choose 1, 2 or 3!" + ANSI_RESET);
        Scanner scanner = new Scanner(System.in);
        int userTermInput = scanner.nextInt();
        System.out.println("*********************************************");
        if (userTermInput == 1) {
            int depositPercent = 9;
            int depositTerm = 3;
            System.out.println(ANSI_RED + "Congratulation! You choose " + depositTerm + " months!" + ANSI_RESET);
            System.out.println(ANSI_RED + "Your deposit percents is " + depositPercent + " now!" + ANSI_RESET);
        } else if (userTermInput == 2) {
            int depositPercent = 10;
            int depositTerm = 6;
            System.out.println(ANSI_RED + "Congratulation! You choose " + depositTerm + " months!" + ANSI_RESET);
            System.out.println(ANSI_RED + "Your deposit percents is " + depositPercent + " now!" + ANSI_RESET);
        } else if (userTermInput == 3) {
            int depositPercent = 11;
            int depositTerm = 12;
            System.out.println(ANSI_RED + "Congratulation! You choose " + depositTerm + " months!" + ANSI_RESET);
            System.out.println(ANSI_RED + "Your deposit percents is " + depositPercent + " now!" + ANSI_RESET);
        } else {
            depositTermUser();
        }
    }



    static void depositSumUser() {
        System.out.println("*********************************************");
        System.out.println(ANSI_GREEN + "What the sum you want to deposit ?" + ANSI_RESET);
        Scanner scanner = new Scanner(System.in);
        int userSumInput = scanner.nextInt();
        if (userSumInput > 0 & userSumInput < 10001) {
            int depositPercent =+ 0;
            System.out.println(ANSI_RED + "Congratulation! You choose " + userSumInput + " money!" + ANSI_RESET);
            System.out.println(ANSI_RED + "Your deposit percents is " + depositPercent + " now!" + ANSI_RESET);
        }
        else if (userSumInput >= 10000 & userSumInput < 20001) {
            int depositPercent =+ 1;
            System.out.println(ANSI_RED + "Congratulation! You choose " + userSumInput + " money!" + ANSI_RESET);
            System.out.println(ANSI_RED + "Your deposit percents is " + depositPercent + " now!" + ANSI_RESET);
        }
        else if (userSumInput > 20000) {
            int depositPercent =+ 3;
            System.out.println(ANSI_RED + "Congratulation! You choose " + userSumInput + " money!" + ANSI_RESET);
            System.out.println(ANSI_RED + "Your deposit percents is " + depositPercent + " now!" + ANSI_RESET);
            System.out.println("*********************************************");
        }
        else {
            depositSumUser();
        }
    }
    public static void main(String[] args) {
        depositTermUser();
        depositSumUser();
    }


    }


