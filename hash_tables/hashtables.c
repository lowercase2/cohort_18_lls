#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#define MAX_NAME 256
#define TABLE_SIZE 15


typedef struct 
{
    char name[MAX_NAME];
    int age;
} person;

person * hash_table[TABLE_SIZE];

unsigned int hash(char *name){
    int length = strlen(name);
    unsigned int hash_value = 0;
    for (int i = 0; i < length; i++){
        hash_value += name[i];
        hash_value = hash_value * name[i] % TABLE_SIZE;
    }
    return hash_value;
}

void init_hash_table() {
    for (int i =0; i < TABLE_SIZE; i++) {
        hash_table[i] = NULL;
    }
}

void print_table() {
    printf("Start\n");
    for (int i =0; i < TABLE_SIZE; i++) {
        if(hash_table[i] == NULL) {
            printf("%d ---\n", i);
        } else {
            printf("%d %s\n",i, hash_table[i]->name);
        }

    }
    printf("end\n");
}

bool hash_table_insert(person *p) {
    if (p == NULL){
        return false;
    }
    // add colission handling(either linear probing or chaining)
    int index = hash(p->name);
    if (hash_table[index] != NULL) {
        return false;
    }
    hash_table[index] = p;
    return true;
}

person *hash_table_get (char *name) {
    int index = hash(name);
    if (hash_table[index] != NULL && strcmp(hash_table[index]->name, name)==0) {
        return hash_table[index];
    } else {
        return NULL;
    }

}
person *hash_table_delete (char *name) {
    int index = hash(name);
    if (hash_table[index] != NULL && strcmp(hash_table[index]->name, name)==0) {
       person *tmp = hash_table[index];
       hash_table[index] = NULL;
       return tmp;
    } else {
        return NULL;
    }

}
int main() {
    
    init_hash_table();
    // print_table();
    person jacob = {"Jacob", 56};
    person john = {"John", 5};
    person james = {"James", 6};
    person julie = {"Julie", 26};

    hash_table_insert(&jacob);
    hash_table_insert(&john);
    hash_table_insert(&james);
    hash_table_insert(&julie);

    print_table();

    person *tmp = hash_table_get("Ali");

    if (tmp == NULL) {
        printf("Not found\n");
    } else {
        printf("found %s.\n", tmp->name);
    }

    hash_table_delete("John");

    tmp = hash_table_get("John");

    if (tmp == NULL) {
        printf("Not found\n");
    } else {
        printf("found %s.\n", tmp->name);
    }

    // printf("John => %u\n", hash("john"));
    // printf("Julie => %u\n", hash("julie"));
    // printf("Joel => %u\n", hash("joel"));
    // printf("Julius => %u\n", hash("julius"));
    // printf("Alice => %u\n", hash("alice"));
    // printf("Ann => %u\n", hash("ann"));
    // printf("Gorge => %u\n", hash("Gorge"));
    // printf("James => %u\n", hash("james"));
    // printf("Ali => %u\n", hash("ali"));
    // printf("Caleb => %u\n", hash("caleb"));
}

