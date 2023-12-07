#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_NAME 256
#define TABLE_SIZE 1024


typedef struct 
{
    char name[MAX_NAME];
    int age;
} person;

unsigned int hash(char *str){
    unsigned long int hash_value;
	int c;

	hash_value = 5381;
	while ((c = *str++))
	{
		hash_value = (((hash_value << 5) + hash_value) + c) % TABLE_SIZE; /* hash * 33 + c */
	}
	return (hash_value);
}

int main() {

    printf("John => %u\n", hash("john"));
    printf("Julie => %u\n", hash("julie"));
    printf("Joel => %u\n", hash("joel"));
    printf("Julius => %u\n", hash("julius"));
    printf("Alice => %u\n", hash("alice"));
    printf("Ann => %u\n", hash("ann"));
    printf("Gorge => %u\n", hash("Gorge"));
    printf("James => %u\n", hash("james"));
    printf("Ali => %u\n", hash("ali"));
    printf("Caleb => %u\n", hash("caleb"));
}

