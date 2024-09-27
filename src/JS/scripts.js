function* generator() {
    var count = 0
    while (true) {
        yield count;
        count++;
        if (count > 9) {
            count = 0;
        }
    }
}

var gen = generator()

for (i = 0; i < 100; i++) {
    console.log(gen.next().value)
}

