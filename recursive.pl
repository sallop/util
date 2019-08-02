%reverse([],[]).
%reverse([H|L],[H|L2]):-reverse(L, L2).

task(1, issue13).
task(2, issue13).
task(3, issue13).

depend_on(X,Y):-task(X, Z).

%parent
%on_hen
