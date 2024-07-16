package main

import (
	"container/list"
	"fmt"
	//"io"
	//"log"
	//"net/http"
)

//  Definition for singly-linked list.
//type ListNode struct {
//Val int
//Next *ListNode
//}

func addTwoNumbers(l1 * list,l2 * list) *list {

	for i := l1.front(); i != nil; i = i.Next() {
		fmt.Println(i)
	}

	fmt.Println("sample")
	return l1
}

func main() {

	l1 := list.New()
	l1.PushBack(1)
	l1.PushBack(2)
	l1.PushBack(3)

	l2 := list.New()
	l2.PushBack(1)
	l2.PushBack(2)
	l2.PushBack(3)
	addTwoNumbers(*l1, *l2)

	/*
			helloHandler := func(w http.ResponseWriter, req *http.Request) {
				io.WriteString(w, "Hello, world!\n")
			}

			http.HandleFunc("/hello", helloHandler)
		    log.Println("Listing for requests at http://localhost:8000/hello")
			log.Fatal(http.ListenAndServe(":8000", nil))
	*/

}
