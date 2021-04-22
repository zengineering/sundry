class Foo {
    var x: Int = 0
        get() {
            field += 1
            return field
        }
    fun bar(y: Int = x):Int = y
}

Foo().apply {
    repeat(3) {
        println(bar())
    }
    println(bar(99))
}

// 1
// 2
// 3
// 99
