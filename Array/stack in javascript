<script>

class twoStacks
{
	// Constructor
	constructor(n)
	{
		this.arr = new Array(n);
		this.size = n;
		this.top1 = Math.floor(n / 2) + 1;
		this.top2 = Math.floor(n / 2);	
	}

// Method to push an element x to stack1
push1(x)
{
	// There is at least one empty
	// space for new element
	if (this.top1 > 0)
	{
	this.top1--;
	this.arr[this.top1] = x;
	}
	else
	{
	document.write("Stack Overflow"
					+ " By element :" + x +"<br>");
	return;
	}
}

// Method to push an element
// x to stack2
push2(x)
{
	// There is at least one empty
	// space for new element
	if (this.top2 < this.size - 1)
	{
	this.top2++;
	this.arr[this.top2] = x;
	}
	else
	{
	document.write("Stack Overflow"
					+ " By element :" + x +"<br>");
	return;
	}
}

// Method to pop an element from first stack
pop1()
{
	if (this.top1 <= this.size / 2)
	{
	let x = this.arr[this.top1];
	this.top1++;
	return x;
	}
	else
	{
	document.write("Stack UnderFlow");
	
	}
	return 0;
}

// Method to pop an element
// from second stack
pop2()
{
	if (this.top2 >= Math.floor(this.size / 2) + 1)
	{
	let x = this.arr[this.top2];
	this.top2--;
	return x;
	}
	else
	{
	document.write("Stack UnderFlow");
	
	}
	return 1;
}

}

/* Driver program to test twStacks class */
let ts = new twoStacks(5);
ts.push1(5);
ts.push2(10);
ts.push2(15);
ts.push1(11);
ts.push2(7);
document.write("Popped element from stack1 is "
				+ " : " + ts.pop1() +"<br>");
ts.push2(40);
document.write("Popped element from stack2 is "
				+ ": " + ts.pop2()
				+"<br>");

// This code is contributed by avanitrachhadiya2155
</script>
